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

    def test_comments(self):
        self.client.login(username='test2', password='1234')

        response = self.client.post('/articles/save/', {'data':json.dumps({'article_id':'',
                                                                  'article_text':'Here we go',
                                                                  'article_name': 'Welcome'})})
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/comments/save/', {'data':json.dumps({'article_id':1,
                                                                  'comment_text': 'lol'})})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'success')

        response = self.client.get('/comments/1/')

        self.assertEqual(response.context['comments'][0]['text'], 'lol')
