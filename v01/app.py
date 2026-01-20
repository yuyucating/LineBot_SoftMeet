import os

from flask import Flask, request, abort, render_template, jsonify

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    FlexMessage, FlexContainer
)
from linebot.v3.webhooks import (MessageEvent, TextMessageContent, PostbackEvent)

from responses import DefaultResponse

key_path = os.path.join(os.path.dirname(__file__), "db.env")
load_dotenv(key_path)

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
secret = os.getenv("LINE_CHANNEL_SECRET")

app = Flask(__name__)

configuration = Configuration(access_token=access_token)
handler = WebhookHandler(secret)

print("★ CONNECTED")

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
    print("★ app.py || message_text()")
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if event.type == "follow" or event.message.text.strip() == "Hi":
            DefaultResponse.Greeting()
            
        
        
@handler.add(PostbackEvent)
def handler_postback(event):
    print("★ app.py || handler_postback()")
    with ApiClient(configuration) as api_client:
        print(f"★ POSTBACK || {event.postback.data}")
        line_bot_api = MessagingApi(api_client)
        
        
if __name__ == "__main__":
    # debug=True 方便開發時 auto reload
    app.run(host="0.0.0.0", port=5000, debug=True)