from django.urls import path
from . import views

urlpatterns = [
    path('<name_slug>/', views.blog_page, name='blog_page'),
    path('', views.blogs_page, name='blogs_page'),

]
