from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getmeetings/', views.getMeetings, name='meetings'),
    path('getresources/', views.getResources, name='resources')
]

