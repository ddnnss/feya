from django.shortcuts import render, get_object_or_404
from .models import EventPage

def event_page(request,name_slug):
    page = EventPage.objects.get(name_slug=name_slug)
    title = page.page_title
    description = page.page_description
    keywords = page.page_keywords
    page_content = page.content
    return render(request, 'pages/index.html', locals())

def events_page(request):
    title = 'Праздничное агентство «Фея74» - организация и проведение праздников в Челябинске'
    description = 'Праздничное агентство «Фея74» предлагает весь комплекс услуг по организации и проведении Ваших праздников в Челябинске уже более 7 лет, команда «Фея74» – это опытные, креативные профессионалы своего дела.'
    keywords = 'праздничное агентство, организация праздников, проведение праздников, праздничное агентство в челябинске, проведение праздников в челябинске'
    return render(request, 'pages/events.html', locals())