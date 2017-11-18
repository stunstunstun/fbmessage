import os
from flask import Flask, request
from fbmessage import Message

app = Flask(__name__)

# assign your facebook accounts info
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN']

message_bot = Message(VERIFY_TOKEN, PAGE_ACCESS_TOKEN)


@app.route("/webhook", methods=['GET'])
def setup():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    else:
        return 'Invalid verification token'


@app.route("/webhook", methods=['POST'])
def callback():
    output = request.get_json()

    for event in output['entry']:
        messaging = event['messaging']
        # each messages
        for x in messaging:
            if x.get('message'):
                recipient_id = x['sender']['id']
                if x['message'].get('text'):
                    text = x['message']['text']
                    # send ping-pong massage
                    message_bot.send_text_message(recipient_id, text)
            else:
                pass
    return "OK"


if __name__ == "__main__":
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
