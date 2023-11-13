from django.test import TestCase
from django.urls import reverse

from message.models import Chat
from message.serializers import serialize_chats


class MessageAppTestCase(TestCase):
    def setUp(self):
        self.chat = Chat.objects.create(
            id=1,
            name='Test chat'
        )

    def testChatSerializer(self):
        serialized_chat = serialize_chats(Chat.objects.all())[0]
        self.assertEqual(serialized_chat['id'], 1),
        self.assertEqual(serialized_chat['name'], 'Test chat'),
        self.assertEqual(serialized_chat['created_at'], self.chat.created_at.strftime("%D %H:%M:%S")),

    def testMessageSerializer(self):
        # todo test
        pass

    def testRenderChatView(self):
        url = reverse('render_chat', kwargs={'chat_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url2 = reverse('render_chat', kwargs={'chat_id': 123})
        response = self.client.get(url2)
        self.assertEqual(response.status_code, 404)

    # todo написать максимально большое кол-во тестов
