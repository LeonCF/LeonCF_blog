from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^article-column/$',views.article_column,name="article_column"),
    url(r'^rename-column/$',views.rename_article_column,name="rename_article_column"),
    url(r'^del-column/$',views.del_article_column,name="del_article_column"),
    url(r'^article-post/$',views.article_post,name="article_post"),
    url(r'^article-list/$',views.article_list,name="article_list"),
]