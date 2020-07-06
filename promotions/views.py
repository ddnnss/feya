from django.shortcuts import render
from .models import Promotion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def promotion_page(request,name_slug):
    page = Promotion.objects.get(name_slug=name_slug)
    title = page.page_title
    description = page.page_description
    keywords = page.page_keywords
    page_content = page.content
    return render(request, 'pages/promotion.html', locals())

def promotions_page(request):
    allNews_temp = Promotion.objects.filter(is_active=True).order_by('-id')
    articlePaginator = Paginator(allNews_temp, 5)
    try:
        allNews = articlePaginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        allNews = articlePaginator.page(1)
    except EmptyPage:
        allNews = articlePaginator.page(articlePaginator.num_pages)
    title = 'Акции | Праздничное агентство «Фея74» - организация и проведение праздников в Челябинске'
    description = 'Праздничное агентство «Фея74» предлагает весь комплекс услуг по организации и проведении Ваших праздников в Челябинске уже более 7 лет, команда «Фея74» – это опытные, креативные профессионалы своего дела.'
    keywords = 'праздничное агентство, организация праздников, проведение праздников, праздничное агентство в челябинске, проведение праздников в челябинске'


    return render(request, 'pages/promotions.html', locals())