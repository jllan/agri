from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'app'
urlpatterns = [
    # url(r'^$', views.question_index, name='index'),
    url(r'^$', views.index, name='index'),
    # url(r'^app/detail/(?P<article_id>\w+)$', cache_page(60 * 15)(views.article_detail), name='detail'),
    # url(r'^app/search/$', views.article_search, name='search'),
    # url(r'^app/tag/(?P<tag_name>.+)$', views.article_tag, name='tag'),
]