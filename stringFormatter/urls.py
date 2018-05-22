from django.urls import path

from . import views

app_name = 'stringFormatter'
urlpatterns = [
        path('', views.index, name='index'),

        path('<int:text_id>/', views.text, name='text'),

        path('<int:text_id>/results', views.result, name='result'),

        path('<int:text_id>/details', views.details, name='details'),

]
