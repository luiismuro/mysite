from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
=======
from django.urls import include, path
>>>>>>> django-admin
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.PostView.as_view(), name='home')


=======
    path('home/', views.PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail')
>>>>>>> django-admin
]
