import unittest
import os
from fbmessage.message import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.verify_token = os.environ['VERIFY_TOKEN']
        self.page_access_token = os.environ['PAGE_ACCESS_TOKEN']
        self.recipient_id = os.environ['RECIPIENT_ID']

    def test_send_text_message(self):
        bot = Message(self.verify_token, self.page_access_token)
        assert bot.send_text_message(self.recipient_id, 'This message is from unittest')