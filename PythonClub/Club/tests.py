from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getMeetings, meetingdetails, getResources

# Create your tests here.


class MeetingTest(TestCase):
    def test_string(self):
        meeting = Meeting(title="Meeting1")
        self.assertEqual(str(meeting), meeting.title)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutes = MeetingMinutes(text="Text")
        self.assertEqual(str(minutes), minutes.text)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class ResourceTest(TestCase):
    def test_string(self):
        resource = Resource(name="Resource1")
        self.assertEqual(str(resource), resource.name)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def test_string(self):
        event = Event(title="Event1")
        self.assertEqual(str(event), event.title)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GetMeetingsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meetings'))
       self.assertEqual(response.status_code, 200)


def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=ProductType.objects.create(typename='laptop')
        self.prod = Product.objects.create(productname='product1', producttype=self.type, user=self.u, productprice=500, productentrydate='2019-04-02', productdescription="a product")
        self.rev1=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod, reviewrating=4, reviewtext='some review')
        self.rev1.user.add(self.u)
        self.rev2=Review.objects.create(reviewtitle='prodreview', reviewdate='2019-04-03', product=self.prod,  reviewrating=4, reviewtext='some review')
        self.rev2.user.add(self.u)