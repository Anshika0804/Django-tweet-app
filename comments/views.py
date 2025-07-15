from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from .forms import CommentForm

# Create your views here.
@login_required
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tweet = tweet
            comment.save()
    return redirect('tweet_list')       