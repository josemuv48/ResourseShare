from django.test import TestCase, Client
from django.urls import reverse
from apps.resources import models
from apps.user.models import User

# Test Case # Test<view-name>View
class TestResourcesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        # TODO: CREATE A USER
        self.user = User.objects.create_user(  # .create_user
            username="kenz",
            password="test@2023password",
            first_name="tony",
            last_name="ralph",
            email="tonyralph@gmail.com",
            bio="Good at anything Python",
            title="Python Developer",
        )
        # TODO: CREATE A TAG
        self.tag = models.Tag(name="Python")
        self.tag.save()  # save it to the database
        # TODO: CREATE A CATEGORY
        self.cat = models.Category.objects.create(cat="Programming Language")
        # TODO: CREATE RESOURCE
        # create without the tag, so that the id is auto generated
        self.resource = models.Resources.objects.create(
            user_id=self.user,
            cat_id=self.cat,
            title="Python for beginners",
            description="All you need to know...",
            link="https://python.com",
        )
        # set the many to many relationship
        self.resource.tag.add(self.tag)
        # save it, so that the changes are recorded in the database
        self.resource.save()
        
        
        
    def test_home_page_return_200_status(self):
        response = self.client.get(
                    reverse('home-page'), # access usl using 
                    HTTP_USER_AGENT='Mozilla/5.0',
                    HTTP_CONTENT_TYPE = 'text/plain'
                    )
        
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_view_resource_count(self):
        # Arrange
        expected_resource_count = 1
        
        response = self.client.get(
                    reverse('home-page'), # access usl using 
                    HTTP_USER_AGENT='Mozilla/5.0',
                    HTTP_CONTENT_TYPE = 'text/plain'
                    )
        self.assertEqual(response.context['cnt'], expected_resource_count)