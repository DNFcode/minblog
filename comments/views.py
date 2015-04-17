from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import Comment
from models import Article
import json


@csrf_exempt
def comments_show(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=article)
    comments_render = [{
        "author": comment.author.username,
        "time": str(comment.created)[:-6],
        "text": comment.comment_text,
        "id": comment.id,
        "commentUser": comment.author
    } for comment in comments]
    return render(request, 'comments.html', {
        'comments': comments_render
    })


@csrf_exempt
def comment_save(request):
    data = json.loads(request.POST.dict()['data'])
    article = Article.objects.get(id=data['article_id'])
    comment = Comment(author=request.user,
                      comment_text=data['comment_text'],
                      article=article)
    comment.save()
    return HttpResponse('success')


@csrf_exempt
def comment_delete(request, id):
    comment = Comment.objects.get(id = id)
    comment.delete()
    return HttpResponse('success')


@csrf_exempt
def comments_update(request):
    data = json.loads(request.POST.dict()['data'])
    article = Article.objects.get(id=data['article_id'])
    comments = Comment.objects.filter(article=article)
    comments = comments[[comment.id for comment in comments].index(data['comment_id'])+1:]
    comments_render = [{
        "author": comment.author.username,
        "time": str(comment.created)[:-6],
        "text": comment.comment_text,
        "id": comment.id,
        "commentUser": comment.author
    } for comment in comments]
    return render(request, 'comments.html', {
        'comments': comments_render
    })