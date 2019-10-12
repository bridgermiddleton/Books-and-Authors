from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.addbooks),
    url(r'^books/(?P<theid>\d+)$', views.renderbooks),
    url(r'^books/addauthors/(?P<theid>\d+)$', views.addauthors),
    url(r'^authors$', views.newauthor),
    url(r'^addauthor$', views.authoradded),
    url(r'^authors/(?P<theid>\d+)$', views.authordetails),
    url(r'^addbook/(?P<theid>\d+)$', views.selectbook),
]