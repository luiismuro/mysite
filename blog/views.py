from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
<<<<<<< HEAD

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world')
=======
from blog.models import Post

class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'    
>>>>>>> django-admin
