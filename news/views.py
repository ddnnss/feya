from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    allNews_temp = News.objects.filter(is_active=True).order_by('-id')
    articlePaginator = Paginator(allNews_temp, 5)
    try:
        allNews = articlePaginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        allNews = articlePaginator.page(1)
    except EmptyPage:
        allNews = articlePaginator.page(articlePaginator.num_pages)
    return render(request, 'pages/news.html', locals())