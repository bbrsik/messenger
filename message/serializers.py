from message.models import Chat


def serialize_chats():
    chats = []
    for chat in Chat.objects.all():
        chats.append({
            'created_at': chat.created_at.strftime("%D %H:%M:%S"),
            'id': chat.id,
            'name': chat.name,
        })
    return chats
