from django.urls import path
from . import views

urlpatterns = [
    path('<name_slug>/', views.news_single_page, name='news_single_page'),
    path('', views.news_page, name='news_page'),

]
