from django.contrib import admin
from django.urls import include, path
from blog.views import PostDetailView, PostListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
