from linebot.v3.messaging import (
    FlexContainer,
    FlexMessage,
    ReplyMessageRequest,
    TextMessage,
    PostbackAction,
    QuickReplyItem,
    MessageAction,
    QuickReply,
    URIAction
)


def Greeting(event, line_bot_api):
    flex_message=FlexMessage(
        alt_text="Hi 陌生人✨ 歡迎加入『微遇』 Soft Meet! 讓我們一起微遇吧!",
        contents=FlexContainer.from_dict(Bubble_Greeting())
    )
    
    line_bot_api.reply_message(
        ReplyMessageRequest(
            reply_token = event.reply_token, messages=[flex_message]
    ))

            
            
def Bubble_Greeting():
    bubble = {
  "type": "bubble", "size": "deca", "hero": {
    "type": "image",
    "url": "https://drive.google.com/thumbnail?id=1tiKOZmRXoa9sWK_JEnRWQj_z9TdNPYci",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://line.me/"
    },
    "align": "center",
    "gravity": "center"
  },
  "body": {
    "type": "box", "layout": "vertical", "contents": [
      {
        "type": "text",
        "text": "微遇 Soft Meet",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "嗨~ 陌生人✨\n一起『微遇』吧！\n\n我們喜歡聚在一起的感覺\n喜歡有人陪伴的感覺\n\n也許只是微笑\n也許，剛剛好心動",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1,
                "wrap": true
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "查看活動",
          "uri": "https://line.me/"
        },
        "color": "#800d00"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Instagram",
          "uri": "https://www.instagram.com/softmeet_official"
        },
        "color": "#c49a86"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
    carousel = {"type": "carousel", "contents": bubble}
    return carousel