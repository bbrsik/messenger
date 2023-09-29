import json

import requests
# broken now
auth_body = {
    'username': 'admin2',
    'password': '123'
}

with requests.session() as session:
    session.post(
        "http://127.0.0.1:8000/message/login/",
        json.dumps(auth_body),
        headers={'Content-Type': 'application/json'}
    )
    body = {
        "chat": 1
    }
    session.post(
        "http://127.0.0.1:8000/message/chat/show/1",
        json.dumps(body),
        headers={'Content-Type': 'application/json'}
    )
