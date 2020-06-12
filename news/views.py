from django.shortcuts import render
from .models import *

def news_single_page(request,name_slug):
    page = News.objects.get(name_slug=name_slug)
    title = page.page_title
    description = page.page_description
    keywords = page.page_keywords
    page_content = page.content
    return render(request, 'pages/news_single.html', locals())

def news_page(request):
    title = 'Праздничное агентство «Фея74» - организация и проведение праздников в Челябинске'
    description = 'Праздничное агентство «Фея74» предлагает весь комплекс услуг по организации и проведении Ваших праздников в Челябинске уже более 7 лет, команда «Фея74» – это опытные, креативные профессионалы своего дела.'
    keywords = 'праздничное агентство, организация праздников, проведение праздников, праздничное агентство в челябинске, проведение праздников в челябинске'
    return render(request, 'pages/news.html', locals())