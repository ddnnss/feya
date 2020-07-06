
from django.urls import path
from . import views

urlpatterns = [
    path('<page_slug>/', views.static_page, name='static_page'),
    path('', views.index, name='index'),




]
