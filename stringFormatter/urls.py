from django.urls import path

from . import views

app_name = 'stringFormatter'
urlpatterns = [
        path('', views.index, name='index'),

        path(r'text/', views.text, name='text'),
        #
        # path('<int:text_id>/results', views.result, name='result'),

        path(r'details/', views.details, name='details'),

]
