from django.shortcuts import get_object_or_404, render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from blog.forms import CommentModelForm
from blog.models import Post

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'


class PostDetailView(View):
    template_name = "post-detail.html"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        comment_form = CommentModelForm()
        return render(request, self.template_name, {
            "post": post,
            "comments": comments,
            "comment_form": comment_form
        })

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True).order_by("-created_on")
        comment_form = CommentModelForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            new_comment = None
        
        return render(request, self.template_name, {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "new_comment": new_comment
        })
