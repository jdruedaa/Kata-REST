from django.contrib.auth.models import User
from django.test import TestCase, Client
import requests


# Create your tests here.
from .models import Image, Portfolio
import json

# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_images_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)
        self.assertEqual(len(current_data),2)

    def test_verify_first_from_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response=self.client.get('/gallery/')
        current_data=json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'],"nuevo")

    def test_add_user(self):
        response=self.client.post('/gallery/addUser/',json.dumps({"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5", "email": "test@test.com"}), content_type='application/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'],'testUser')

    def test_list_portafolio_status(self):
        url = '/gallery/portfolios/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_portfolios_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test', last_name='test', email='test@test.com')
        img1 = Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        img2 = Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)
        p1 = Portfolio.objects.create(privacidades=["publico", "privado"], user=user_model)
        p1.imagenes.add(img1.id)
        p1.imagenes.add(img2.id)
        p2 = Portfolio.objects.create(privacidades=["publico", "privado"], user=user_model)
        p2.imagenes.add(img1.id)
        p2.imagenes.add(img2.id)

        response = self.client.get('/gallery/portfolios/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

    def test_add_user2(self):
        response=self.client.post('/gallery/addUser/',json.dumps({"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5", "email": "test@test.com"}), content_type='application/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'],'testUser')