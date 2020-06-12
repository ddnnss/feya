from django.urls import path
from . import views

urlpatterns = [
    path('<name_slug>/', views.event_page, name='event_page'),
    path('', views.events_page, name='events_page'),

]
