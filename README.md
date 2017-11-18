
[![Build Status](https://travis-ci.org/stunstunstun/fbmessage.svg?branch=master)](https://travis-ci.org/stunstunstun/fbmessage)

## fbmessage

fbmessage helps you use the Facebook Messenger API in Python.

### Install

First to use fbmessage in your environment, you can install the module as shown below. request module is required to use fbmessage. 

````
pip install requests
pip install fbmessage
````

### Quick Start

To use the API provided by Facebook Messenger platform, the following environment variables must be registered in the operating system.

Constants | Description
--|--
VERIFY_TOKEN | Verification token used in Facebook Application Page
PAGE_ACCESS_TOKEN | Access token to use Messenger API on Facebook Page

### Send Message

#### Message.send_text_message(recipient_id, text)

Parameters | Description 
--|--
recipient_id | User ID that receives the message
text | Message to send to user

#### Examples

````python
from fbmessage import Message

message_bot = Message(VERIFY_TOKEN, PAGE_ACCESS_TOKEN)
message_bot.send_text_message(recipient_id, text)
````

