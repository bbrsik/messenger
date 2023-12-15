from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from message.models import Chat, Message
from message.serializers import serialize_chats, serialize_messages
from django.urls import reverse


class SerializersTestCase(TestCase):
    def setUp(self):
        # serialize_chats test setup
        self.chat = Chat.objects.create(
            id=1,
            name='Test chat'
        )

        # serialize_messages test setup
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.message1 = Message.objects.create(
            user=self.user1,
            chat=self.chat,
            text='text1',
        )
        self.message2 = Message.objects.create(
            user=self.user2,
            chat=self.chat,
            text='text2',
            reply_on=self.message1,
        )

    def test_serialize_chats(self):
        serialized_chat = serialize_chats(Chat.objects.all())[0]
        self.assertEqual(serialized_chat['id'], 1),
        self.assertEqual(serialized_chat['name'], 'Test chat'),
        self.assertEqual(serialized_chat['created_at'], self.chat.created_at.strftime("%D %H:%M:%S")),

    def test_serialize_messages(self):
        serialized_message1 = serialize_messages(Message.objects.all())[0]
        self.assertEqual(serialized_message1['username'], 'user1'),
        self.assertEqual(serialized_message1['text'], 'text1'),
        self.assertEqual(serialized_message1['created_at'], self.message1.created_at.strftime("%D %H:%M:%S")),

        serialized_message2 = serialize_messages(Message.objects.all())[1]
        self.assertEqual(serialized_message2['username'], 'user2'),
        self.assertEqual(serialized_message2['text'], 'text2'),
        self.assertEqual(serialized_message2['replies_history'],
                         serialize_messages(self.message2.get_replies_history())),
        self.assertEqual(serialized_message2['created_at'], self.message2.created_at.strftime("%D %H:%M:%S")),


class RenderViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='1234')
        self.client.login(username='testuser', password='1234')

        self.chat = Chat.objects.create(
            id=1,
            name='Test chat'
        )

    def test_render_chat(self):
        url = reverse('render_chat', kwargs={'chat_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url2 = reverse('render_chat', kwargs={'chat_id': 123})
        response = self.client.get(url2)
        self.assertEqual(response.status_code, 404)
        # smoke test

    def test_render_list(self):
        url = reverse('render_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ApiViewsTestCase(TestCase):
    def setUp(self):
        # create_chat test
        pass
    pass
