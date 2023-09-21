import requests


requests.post("http://127.0.0.1:8000/message/create/",
              '{"message": "test text"}',
              headers={'Content-Type': 'application/json'})
