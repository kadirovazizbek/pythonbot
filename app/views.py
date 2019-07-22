import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
@csrf_exempt
def index(request):
	req = json.loads(request.body)
	msg = {'chat_id' : 2152388, 'text' : 'helloworld'}
	response = sendMessage(2152388, 'hello World!')
	return HttpResponse(response)

def sendMessage(chat_id, text):
	params = {'text' : text}
	response = send_request('sendMessage', chat_id, params)
	return response

def send_request(method, chat_id, params):
	url = "https://api.telegram.org/bot813824290:AAEIU_yRvsfIgncPfvl9Oz_iKw0_qiKXeog/"+method
	params["chat_id"] = chat_id
	response = requests.post(url, params=params)
	return response