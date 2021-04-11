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
		"午安":['https://www.dropbox.com/s/3q7a8ge4yl775wh/_6914331.m4a?dl=0', 'https://www.dropbox.com/s/y0d2vk3dgul2ejd/_6914332.m4a?dl=0', 'https://www.dropbox.com/s/ux9sv8050ftx6w4/_6914333.m4a?dl=0', 'https://www.dropbox.com/s/r09k1z494zco42k/_6914334.m4a?dl=0', 'https://www.dropbox.com/s/cle23ix5qukesmn/_6914335.m4a?dl=0', 'https://www.dropbox.com/s/ouo4xj0vmaqvr4v/_6914336.m4a?dl=0'], 
		"晚安":['https://www.dropbox.com/s/m5db7oygjo35xj2/_6914338.m4a?dl=0', 'https://www.dropbox.com/s/k3mlfx7yxdjieb2/_6914339.m4a?dl=0', 'https://www.dropbox.com/s/0g2756kmz4kt8uh/_6914340.m4a?dl=0', 'https://www.dropbox.com/s/0lxj7g4rvnrz650/_6914341.m4a?dl=0', 'https://www.dropbox.com/s/aatu4ojsx27lx5k/_6914342.m4a?dl=0', 'https://www.dropbox.com/s/thjnnr7wo9tl1dv/_6914343.m4a?dl=0'], 
		"唸書":['https://www.dropbox.com/s/aoew8kpk5uw2eb3/_6914345.m4a?dl=0', 'https://www.dropbox.com/s/xh5hrkyd4m7c316/_6914346.m4a?dl=0', 'https://www.dropbox.com/s/v4msc1ffrwar1h5/_6914347.m4a?dl=0', 'https://www.dropbox.com/s/pn8bhzrjpdgrdaz/_6914348.m4a?dl=0', 'https://www.dropbox.com/s/wp8oe5jq89xr4at/_6914349.m4a?dl=0'], 
		"吃飯":['https://www.dropbox.com/s/jhicd9xui5mkfl3/_6914351.m4a?dl=0', 'https://www.dropbox.com/s/pnb1doyll9x0zwi/_6914352.m4a?dl=0', 'https://www.dropbox.com/s/r5wnedsvrbhwd02/_6914353.m4a?dl=0', 'https://www.dropbox.com/s/4wd8yfij3konh07/_6914354.m4a?dl=0', 'https://www.dropbox.com/s/dtnw9pgieldd4c9/_6914355.m4a?dl=0'], 
		"睡不著":['https://www.dropbox.com/s/rvaa7icw1jok9pm/_6914357.m4a?dl=0', 'https://www.dropbox.com/s/5kuq1ss5x2zfj3o/_6914358.m4a?dl=0', 'https://www.dropbox.com/s/ywy9njvan1ljuri/_6914359.m4a?dl=0', 'https://www.dropbox.com/s/77q0n61scmrug72/_6914360.m4a?dl=0', 'https://www.dropbox.com/s/lhwunhy4axzkwa5/_6914361.m4a?dl=0', 'https://www.dropbox.com/s/ucpf96f217xaox9/_6914362.m4a?dl=0']}


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








