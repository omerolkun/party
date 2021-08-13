from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index-page'),
    path('columnist_article/<int:colid>',views.articles,name='articles-page'),
    path('article/<int:arid>',views.articleDetail,name='article-detail-page'),
    path('article_index/',views.articleIndex,name='article-index-page'),
    path('new_columnist/',views.newColumnist,name='new-columnist-page'),
    path('register/',views.register,name='register-page'),
    path('users/',views.userList,name='user-list-page'),
]