from django.urls import path

from . import views

app_name = 'stringFormatter'
urlpatterns = [
        path('', views.index, name='index'),

        path(r'formatter/', views.formatter, name='formatter'),

]
