from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .views import ToDoViewSet


# Create your tests here.

class TestToDoViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todos/')
        view = ToDoViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        factory = APIRequestFactory()
        request = factory.post('/api/todos/')
        view = ToDoViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

