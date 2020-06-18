from django.shortcuts import render
from .models import *

def blog_page(request,name_slug):
    page = Blog.objects.get(name_slug=name_slug)
    title = page.page_title
    description = page.page_description
    keywords = page.page_keywords
    page_content = page.content
    return render(request, 'pages/blog.html', locals())

def blogs_page(request):
    title = 'Праздничное агентство «Фея74» - организация и проведение праздников в Челябинске'
    description = 'Праздничное агентство «Фея74» предлагает весь комплекс услуг по организации и проведении Ваших праздников в Челябинске уже более 7 лет, команда «Фея74» – это опытные, креативные профессионалы своего дела.'
    keywords = 'праздничное агентство, организация праздников, проведение праздников, праздничное агентство в челябинске, проведение праздников в челябинске'
    allBlogs = Blog.objects.filter(is_active=True)
    return render(request, 'pages/blogs.html', locals())