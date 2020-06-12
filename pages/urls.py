
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<page_slug>/', views.static_page, name='static_page'),



]
