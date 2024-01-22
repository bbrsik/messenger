from django.test import TestCase
from django.contrib.auth.models import User
from message.models import Chat


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='1234')

    def test_logged_in_redirect(self):
        self.client.login(username='testuser', password='1234')
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_not_logged_in_redirect(self):
        self.client.login(username='testuser', password='1111')
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_successful_login(self):
        response = self.client.post('/user/api/login/', {'username': 'testuser', 'password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_failed_login(self):
        response = self.client.post('/user/api/login/', {'username': 'testuser', 'password': '1111'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.client.session['login_failed'])
