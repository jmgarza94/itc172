from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),

    path('getmeetings/', views.getMeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),

    path('getresources/', views.getResources, name='resources')
]

