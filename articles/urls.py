from django.conf.urls import url

from .views import (
    index,  # import method index from articles/views.py
    detail,
    create,
    update,
    delete,
)


urlpatterns = [
    url(r'^$', index, name='index'),  # pointing localhost:8000/articles to method index in articles/views.py
    #  pointing for example localhost:8000/articles/1 to method detail & get article detail with id 1
    url(r'^(\d+)/$', detail, name='detail'),
    url(r'^create$', create, name='create'),
    url(r'^(\d+)/update$', update, name='update'),
    url(r'^(\d+)/delete$', delete, name='delete'),
]