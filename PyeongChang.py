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

def get_price_list(session_code):
	url = "https://ticketapi.pyeongchang2018.com/api/Session/GetSessionPriceList/?Culture=ko-kr&SessionCode=" + session_code
	req = requests.get(url)	
	res = req.json()["data"]
	return res

def get_session_info_row(session_info):
	keys = ["DisciplineName", "EventName", "StartDate", "StartTime", "EndTime", "ClusterName", "VenueName"]
	row = []
	for key in keys:
		row.append(session_info[key].replace("\n","").strip())		
	return row

def get_price_list_row(price_list):	
	keys = ["SalesPrice", "GP_SeatCount"]
	row = []
	for price in price_list:		
		if price["PriceName"] == u"일반":
			for key in keys:
				row.append(str(price[key]).replace("\n","").strip())
	return row	

rows = []
session_list = get_session_list()
for session in session_list:
	session_code = session["SessionCode"]		
	session_info = get_session_info(session_code)
	price_list = get_price_list(session_code)
	row = get_session_info_row(session_info)	
	row.extend(get_price_list_row(price_list))
	rows.append(row)	

import unicodecsv
file = open("tickets.csv", "wb")
writer = unicodecsv.writer(file, encoding="utf-8", lineterminator="\n")
header = ["종목","경기","날짜","시작","종료","장소","경기장","A가격","A잔여","B가격","B잔여","C가격","C잔여","D가격","D잔여"]
writer.writerow(header)
for row in rows:	
	writer.writerow(row)	