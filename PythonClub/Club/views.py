from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'PythonClub/index.html')

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'PythonClub/meetings.html',{'meeting_list' : meeting_list})

def getResources(request):
    resource_list=Resource.objects.all()
    return render(request, 'PythonClub/resources.html',{'resource_list' : resource_list})