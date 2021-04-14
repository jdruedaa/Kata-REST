from django.contrib.auth.models import User
from django.test import TestCase, Client
import requests

# Create your tests here.
from .models import Image, Portfolio, Portfolio_Image
import json


# Create your tests here.
class GalleryTestCase(TestCase):

    def test_list_images_status(self):
        url = '/gallery/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

    def test_verify_first_from_images_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)

        response = self.client.get('/gallery/')
        current_data = json.loads(response.content)

        self.assertEqual(current_data[0]['fields']['name'], "nuevo")

    def test_add_user(self):
        response = self.client.post('/gallery/addUser/', json.dumps(
            {"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5",
             "email": "test@test.com"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'testUser')

    def test_list_portafolio_status(self):
        url = '/gallery/portfolios/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_portfolios_list(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        img1 = Image.objects.create(name='nuevo', url='No', description='testImage', type='jpg', user=user_model)
        img2 = Image.objects.create(name='nuevo2', url='No', description='testImage', type='jpg', user=user_model)
        p1 = Portfolio.objects.create(user=user_model)
        Portfolio_Image.objects.create(imagen=img1, privacidad=0, portfolio=p1)
        Portfolio_Image.objects.create(imagen=img2, privacidad=1, portfolio=p1)
        p2 = Portfolio.objects.create(user=user_model)
        Portfolio_Image.objects.create(imagen=img1, privacidad=1, portfolio=p2)
        Portfolio_Image.objects.create(imagen=img2, privacidad=0, portfolio=p2)

        response = self.client.get('/gallery/portfolios/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

    def test_add_user2(self):
        response = self.client.post('/gallery/addUser/', json.dumps(
            {"username": "testUser", "first_name": "Test", "last_name": "User", "password": "AnyPas#5",
             "email": "test@test.com"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'testUser')

    def test_portfolios_public_data(self):
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        img1 = Image.objects.create(name='nuevo3', url='No', description='testImage', type='jpg', user=user_model)
        img2 = Image.objects.create(name='nuevo4', url='No', description='testImage', type='jpg', user=user_model)
        p1 = Portfolio.objects.create(user=user_model)
        Portfolio_Image.objects.create(imagen=img1, privacidad=0, portfolio=p1)
        Portfolio_Image.objects.create(imagen=img2, privacidad=1, portfolio=p1)
        p2 = Portfolio.objects.create(user=user_model)
        Portfolio_Image.objects.create(imagen=img1, privacidad=1, portfolio=p2)
        Portfolio_Image.objects.create(imagen=img2, privacidad=0, portfolio=p2)

        response = self.client.get('/gallery/portfolios/')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['imagenesPublicas'], [6])
        self.assertEqual(current_data[1]['fields']['imagenesPublicas'], [5])

    def test_user_login(self):
        user_model = User.objects.create_user(username='test3', password='12345', first_name='test3', last_name='test3', email='test3@test.com')
        login = self.client.login(username='test3', password='12345')
        url = '/gallery/loguser/'
        response=self.client.post(url, json.dumps({"username": "test3", "password": "12345"}), content_type='application/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'],'test3')
        self.assertEqual(response.status_code, 200)
