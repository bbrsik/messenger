from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from message.models import Chat


class LoginTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='1234')

    def test_successful_login(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.post('/user/login/', {'username': 'testuser', 'password': '1234'})
        self.assertRedirects(response, '/message/chats/')
        self.client.logout()

    def test_failed_login(self):
        self.client.login(username='testuser', password='1111')
        response = self.client.post('/user/login/', {'username': 'testuser', 'password': '1111'})
        self.assertEqual(response.status_code, 200)
        self.client.logout()
