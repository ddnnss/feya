from django.urls import path
from . import views

urlpatterns = [
    path('<name_slug>/', views.promotion_page, name='promotion_page'),
    path('', views.promotions_page, name='promotions_page'),

]
