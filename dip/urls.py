from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index-page'),
    path('columnist_article/<int:colid>',views.articles,name='articles-page'),
    path('article/<int:arid>',views.articleDetail,name='article-detail-page'),
    path('article_index/',views.articleIndex,name='article-index-page'),
]