#-*- coding: utf-8 -*-
import requests

def get_session_list():
	url = "https://tickets.pyeongchang2018.com/Session/GetSessionList";
	payload = {
		"Culture":"ko-kr",
		"SDate":"2018-02-08",
		"EDate":"2018-02-25",
		"SearchKey":"",
		"SeatCount":0,
		"Disciplines":"",
		"Genders":"",
		"Times":"",
		"Stadiums":"",
		"Medal":""
	}
	req = requests.post(url, json=payload)
	res = req.json()
	return res

def get_session_info(session_code):
	url = "https://ticketapi.pyeongchang2018.com/api/Session/GetSession/?Culture=ko-kr&SessionCode=" + session_code
	req = requests.get(url)
	res = req.json()
	return res	

session_list = get_session_list()
for session in session_list:
	session_code = session["SessionCode"]
	session_info = get_session_info(session_code)	
	print session_info