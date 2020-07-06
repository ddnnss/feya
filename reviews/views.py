from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def feedbacks(request):
    title = 'Отзывы | Праздничное агентство «Фея74» - организация и проведение праздников в Челябинске'
    description = 'Праздничное агентство «Фея74» предлагает весь комплекс услуг по организации и проведении Ваших праздников в Челябинске уже более 7 лет, команда «Фея74» – это опытные, креативные профессионалы своего дела.'
    keywords = 'праздничное агентство, организация праздников, проведение праздников, праздничное агентство в челябинске, проведение праздников в челябинске'

    allNews_temp =  Feedback.objects.all().order_by('-id')
    articlePaginator = Paginator(allNews_temp, 5)
    try:
        allNews = articlePaginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        allNews = articlePaginator.page(1)
    except EmptyPage:
        allNews = articlePaginator.page(articlePaginator.num_pages)
    return render(request, 'pages/feedbacks.html', locals())
