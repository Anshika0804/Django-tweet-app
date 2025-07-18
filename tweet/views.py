from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from rest_framework import viewsets, permissions
from .serializers import TweetSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')

# def tweet_list(request):
#     tweets = Tweet.objects.all().order_by('-created_at')
#     return render(request, 'tweet_list.html', {'tweets' : tweets})

def tweet_list(request):
    query = request.GET.get('q')

    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains = query) |
            Q(user__username__icontains = query)
        ).order_by('created_at')
    else:
        tweets = Tweet.objects.all().order_by('created_at')

    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'query': query  
    })

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form' : form})

@login_required   
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance = tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance = tweet)
    return render(request, 'tweet_form.html', {'form' : form}) 

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet' : tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})

@login_required
def my_tweets(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'my_tweets.html', {'tweets': tweets})

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

