from django.shortcuts import render, redirect
from django.utils import timezone

from django.views import generic

from .models import Post, Comment
from .forms import PostForm, CommentForm


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    
class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"
    
    
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')  # Redirect to the home page after saving the post
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

    
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.comment_date = timezone.now()  # Set the current date and time
            comment.save()
            return redirect('blog:detail', pk=post_id)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})


