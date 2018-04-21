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

res = get_session_list()
print res