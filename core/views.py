from django.shortcuts import render, get_object_or_404
from . import models
from .models import News, Weather, Category
from django.core.paginator import Paginator
from datetime import date



def index(request):
    today = date.today()
    news_header = News.objects.all()
    news_post = News.objects.all().order_by('-created_at')
    categories = Category.objects.filter(type='category')
    weather = Weather.objects.all()
    languages = Category.objects.filter(type='language')

    q = request.GET.get('q')
    category = request.GET.get('category')
    language = request.GET.get('language')
    if q:
        news_post = News.objects.filter(title__icontains=q).order_by('-created_at')

    if category:
        news_post = News.objects.filter( category__title=category).order_by('-created_at')
        
    if language:
        news_post = News.objects.filter( category__title=language).order_by('-created_at')
   
    paginator = Paginator(news_post, 6)
    page_number = request.GET.get('page')
    news_post = paginator.get_page(page_number)
    context = {
        'weather': weather,
        'categories':categories,
        'news_header':news_header,
        'languages':languages,
        'today':today,
        'news_post':news_post,
    }
    
    return render(request, 'index.html', context)

def blog_detail(request, id):
    today = date.today()
    news_header = News.objects.all()
    news = News.objects.all()
    blog = get_object_or_404(News, id=id)
    related_news = News.objects.filter(category=blog.category).exclude(id=blog.id).order_by('-created_at')[:5]
    q = request.GET.get('q')
    if q:
        news = news.filter(title__icontains=q)

    category = request.GET.get('category')
    language = request.GET.get('language')
    if category:
        news = Category.objects.filter(type='category')
        
    if language:
        news = Category.objects.filter(type='language')

    categories = Category.objects.filter(type='category')
    weather = Weather.objects.all()
    languages = Category.objects.filter(type='language')
    
    weather = Weather.objects.all()
    blog.view_count += 1
    blog.save()
    context = {
        'blog':blog,
        'news':news,
        'related_news': related_news,
        'weather': weather,
        'categories':categories,
        'news_header':news_header,
        'today':today,
        'languages':languages
    }
    return render(request, 'blog_detail.html',context)
