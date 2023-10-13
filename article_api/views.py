from django.shortcuts import render
from django.http import JsonResponse
from article_api.models import Article
from article_api.serializers import ArticleSerializer

# Create your views here.
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return JsonResponse(serializer.data, safe=False)
        