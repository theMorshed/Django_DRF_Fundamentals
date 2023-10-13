from django.urls import path
from article_api.views import article_list

urlpatterns = [
    path('article/', article_list),
]
