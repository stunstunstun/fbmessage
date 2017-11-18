"""
Facebook Message API Implement
"""
from .constants import GRAPH_API
import requests
import json


class Message(object):
    def __init__(self, verify_token, page_access_token):
        self.verify_token = verify_token
        self.page_access_token = page_access_token

    def send_text_message(self, recipient_id, text):
        url = GRAPH_API + '?access_token=' + self.page_access_token
        headers = {'Content-Type': 'application/json'}
        body = {'recipient': {'id': recipient_id}, 'message': {'text': text}}
        return requests.post(url, data=json.dumps(body), headers=headers)

