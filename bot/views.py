import json
import requests
from django.conf import settings 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Message, Chat

# Create your views here.
chat = Chat()
@csrf_exempt
def index(request):
	req = json.loads(request.body)
	message_text = req['message']['text']
	
	chat.id = req['message']['from']['id']
	chat.username = req['message']['from']['username']
	chat.first_name = req['message']['from']['first_name']
	chat.last_name = req['message']['from']['last_name']
	chat.save()
	
	message = Message()
	message.message_id = req['message']['message_id']
	message.chat = chat
	message.text = message_text
	message.my_in = 1
	message.save()

	if "/start" in message_text:
		response_str = "Welcome to my bot!"
	elif "/stop" in message_text:
		response_str = "Good bye!"
	elif "/help" in message_text:
		response_str = "We don't help our users..."
	else:
		response_str = "We didn't recognize your command"

	response = sendMessage(req['message']['chat']['id'], response_str)
	#response = sendPhoto(req['message']['chat']['id'], 'photo.jpg')
	return HttpResponse("")

def sendMessage(chat_id, text):
	params = {'text' : text}
	response = send_request('sendMessage', chat_id, params)
	response_obj = response.json()
	#print(response_obj)
	if response_obj['ok'] == True:
		msg = Message()
		msg.message_id = response_obj['result']['message_id']
		msg.text = text
		msg.my_in = 0
		msg.chat = chat
		msg.save()
	return response

def editLastMessageText(chat_id, new_text):
	lastMessage = Message.objects.filter(my_in = 1).order_by('-id')[:1]
	message_id = lastMessage.message_id
	params = {'text' : new_text, 'message_id' : message_id}
	response = send_request('editMessageText', chat_id, params = params)
	return response

def sendPhoto(chat_id, photo_path):
	response = send_request(method = 'sendPhoto', chat_id = chat_id, file_path = photo_path)
	return response

def send_request(method, chat_id, params = {}, file_path = False):
	url = "https://api.telegram.org/bot" + settings.BOT_API_KEY + '/' + method
	#print(url)
	params["chat_id"] = chat_id
	keyboard = [
		[
			{'text' : 'hello', 'callback_data' : 'abc'}, {'text': 'second', 'callback_data' : 'abc'},
		],
		[
			{'text' : 'test', 'callback_data' : 'abc'}, {'text': 'jdkfjld', 'callback_data' : 'abc'}
		]
	]
	params["reply_markup"] = array_to_keyboard(keyboard)
	if file_path != False:
		file = dict(photo=open(file_path, 'rb'))
		response = requests.post(url, params=params, files=file, verify=False)
	else:
	    response = requests.post(url, params=params, verify=False)

	return response

def array_to_keyboard(buttons):
	kbd = []
	kbd = json.dumps({
		'inline_keyboard' : buttons
	})
	return kbd