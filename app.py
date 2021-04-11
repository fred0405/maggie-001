# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, flex_message
from linebot.models import *
import random

    
app = Flask(__name__)


line_bot_api = LineBotApi('Jb3cS2e1C1ihbAM38Vv/CBl3fgPkIm22CesgJsrMjjrLXPKr102lOBVLXk7gSvOGT0nCcVRiIqVqdWt9kqwvg4ChHUliu23KzQNbH54dWW6XthIgNmQ16EIzXsbiTMSZSFzyqv4iv7EyP5TPVQTx4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58acda0f2c42346d072457c2e8fd39f3')

msg_type = ["早安", "午安", "晚安", "唸書", "吃飯", "睡不著"]
msg_data = {"早安":['https://www.dropbox.com/s/3twgnopog0i60gx/_6914312.m4a?dl=0', 'https://www.dropbox.com/s/do3fixcjp6qcaib/_6914313.m4a?dl=0', 'https://www.dropbox.com/s/0cqls86lgjec2od/_6914314.m4a?dl=0', 'https://www.dropbox.com/s/p7cbyfih9h6ukwt/_6914315.m4a?dl=0', 'https://www.dropbox.com/s/cry1isljb2d3j93/_6914316.m4a?dl=0', 'https://www.dropbox.com/s/0ob0cn930vz9kqb/_6914317.m4a?dl=0'], 
		"午安":[], 
		"晚安":[], 
		"唸書":[], 
		"吃飯":[], 
		"睡不著":[]}


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
	if event.message.text not in msg_type:
		print('out of range')
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "現在還沒支援那麼多！！！"))
	else:
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text = random.choice(msg_data[event.message.text])))

	
	
	



if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000, debug=True)








