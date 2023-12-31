from django.urls import path
# from article_api.views import article_list, article_detail, ArticleList, ArticleDetails
from article_api.views import ArticleList, ArticleDetails

urlpatterns = [
    # path('article/', article_list), # for functional view and with decorator functional view
    # path('article/<int:pk>/', article_detail)
    # path('article/', ArticleList.as_view()),
    # path('article/<int:pk>/', ArticleDetails.as_view()),
    path('article/', ArticleList.as_view()),
    path('article/<int:pk>/', ArticleDetails.as_view()),
]
