from django.urls import path
from article_api.views import article_list, article_detail

urlpatterns = [
    path('article/', article_list),
    path('details/<int:pk>/', article_detail)
]
