from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from models import Article
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def article_save(request):
    return HttpResponse("LOL")


@csrf_exempt
def articles_show(request):
    articles = list(Article.objects.all())
    articles.sort(key=lambda x: x.id ,reverse=True)
    return render(request, 'show_articles.html', {
        'articles': articles
    })


@csrf_exempt
def article_save(request):
    data = json.loads(request.POST.dict()['data'])
    if(data['article_id'] != ''):
        article = Article.objects.get(id=int(data['article_id']))
        article.article_name = data['article_name']
        article.article_text = data['article_text']
    else:
        article = Article(author = request.user,
                          article_text = data['article_text'],
                          article_name = data['article_name'])
    article.save()
    return HttpResponse('success')


@csrf_exempt
def article_create(request):
    return render(request, 'create_article.html')


@csrf_exempt
def article_show(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'show_articles.html', {
        'articles': [article]
    })


@csrf_exempt
def article_change(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'create_article.html', {
        'article': article
    })


@csrf_exempt
def article_delete(request):
    data = json.loads(request.POST.dict()['data'])
    try:
        article = Article.objects.get(id=data['article_id'])
        article.delete()
        return HttpResponse('success')
    except(Exception):
        return HttpResponse('bad')