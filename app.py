# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, flex_message
from linebot.models import *
from get_data import crawler

    
app = Flask(__name__)

cr = crawler()

line_bot_api = LineBotApi('Jb3cS2e1C1ihbAM38Vv/CBl3fgPkIm22CesgJsrMjjrLXPKr102lOBVLXk7gSvOGT0nCcVRiIqVqdWt9kqwvg4ChHUliu23KzQNbH54dWW6XthIgNmQ16EIzXsbiTMSZSFzyqv4iv7EyP5TPVQTx4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58acda0f2c42346d072457c2e8fd39f3')

@app.route('/', methods = ['GET'])
def hello():
	return "Hello World!"

@app.route('/callback', methods = ['POST'])
def callback():
	signature = request.headers['X-Line-Signature']

	body = request.get_data(as_text = True)
	print("Request body: " + body, "Signature: " + signature)

	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)

	return 'OK'

@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
	msg = event.message.text
	msg = msg.encode('utf-8')
	# if event.message.text == '文字':
	# 	print('收到文字')
	# 	line_bot_api.reply_message(event.reply_token, TextSendMessage(text = event.message.text))
	
	data = cr.get_data(event.message.text)
	
	if data == "not found":
		result = "料號錯誤"
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text = result))

	else:
		
		column = list()
		for item in data:
			result = ""
			for key in item:
				if key != '下單網址' and key != '詳細頁面':
					result = result + key + ' ' + item[key] + '\n'
			column.append(CarouselColumn(text = result,
				actions=[URITemplateAction(label='立即詢料', uri=item['下單網址']), 
				PostbackTemplateAction(label='詳細資訊', data = item['詳細頁面'] + ' ' + item['下單網址'])]
			))
		Carousel_template = TemplateSendMessage(alt_text="Carousel template", template=CarouselTemplate(
			columns=column))
		# print(Carousel_template)
		line_bot_api.reply_message(event.reply_token, Carousel_template)

@handler.add(PostbackEvent)
def handle_postback(event):
	print(event.postback.data)
	postback_data = event.postback.data.split(' ')
	print("success")
	data = cr.get_info(postback_data[0])
	print(data)
	result = ''
	for key in data:
		result += key + ' ' + data[key] + '\n'
	result = result.strip()
	buttons_template = TemplateSendMessage(alt_text="Buttons template", template=ButtonsTemplate(text=result,
		actions=[URITemplateAction(label='立即詢料', uri=postback_data[1])]
		))
	line_bot_api.reply_message(event.reply_token, buttons_template)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000, debug=True)








