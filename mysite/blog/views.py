from django.shortcuts import render

from django.views import generic

from .models import Post, Comment


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    
class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"
    



# def index(request):
#     return HttpResponse("THIS IS A BLOG!!!")

# Create your views here.
