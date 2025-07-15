from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from .forms import CommentForm
from .models import Comment

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

@login_required
def comment_list(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = tweet.comments.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.tweet = tweet
            new_comment.save()
            return redirect('comment_list', tweet_id=tweet.id)

    return render(request, 'comments/comment_list.html', {
        'tweet': tweet,
        'comments': comments,
        'form': form,
    })




@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return redirect('tweet_list')  # deny editing if not author

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comments.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user:
        comment.delete()

    return redirect('tweet_list')


