from django.test import TestCase

from django.test import Client

from django.contrib.auth.models import User

import json


class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        user = User(username='test2',
                email='test2@test.tst')
        user.set_password('1234')
        user.save()

    def tearDown(self):
        user = User.objects.get(username='test2')
        user.delete()

    def test_register(self):
        response = self.client.post('/user/register/', {'username': 'test',
                                                        'email': 'test@test.tst',
                                                        'password': '1234'})
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/user/register/', {'username': 'test',
                                                        'email': 'test@test.tst',
                                                        'password': '1234'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'WRONG')

    def test_login(self):
        response = self.client.post('/user/login/', {'username': 'test2',
                                                     'password': '1234'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.wsgi_request.user.username, 'test2')

        response = self.client.post('/user/login/', {'username': 'tes',
                                                     'password': '1234'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Wrong username and password.')

    def test_logout(self):
        self.client.login(username='test2', password='1234')

        response = self.client.get('/user/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.wsgi_request.user.username, '')
