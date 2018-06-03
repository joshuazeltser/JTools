from django.urls import path

from . import views

app_name = 'stringFormatter'
urlpatterns = [
        path('', views.index, name='index'),
        path(r'formatter/', views.formatter, name='formatter'),
        path(r'about/', views.about, name='about'),
        path(r'randomiser/', views.randomiser, name='randomiser'),
        path(r'pdfeditor/', views.pdfeditor, name='pdfeditor'),
        url(r'^.well-known/acme-challenge/.*$',
            views.acme_challenge, name='acme-challenge'),

]
