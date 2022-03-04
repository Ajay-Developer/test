from django.urls import path
from calc import views

app_name='calc'

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]