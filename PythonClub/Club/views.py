from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm

# Create your views here.
def index (request):
    return render(request, 'PythonClub/index.html')

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'PythonClub/meetings.html',{'meeting_list' : meeting_list})

def meetingdetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    # minutes=get_object_or_404(MeetingMinutes, meetingid=meeting.id)
    # discount=prod.memberdiscount
    # reviews=Review.objects.filter(product=id).count()
    context={
        'meeting' : meeting,
        'minutes' : "to-do",
    }
    return render(request, 'PythonClub/meetingdetails.html', context=context)

def getResources(request):
    resource_list=Resource.objects.all()
    return render(request, 'PythonClub/resources.html',{'resource_list' : resource_list})


def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'PythonClub/newmeeting.html', {'form': form})