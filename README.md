# PyeongChang
Crawl, Parse, Save ticket data from PyeongChang winter olympic website

# Requirements
- python 2.7.14
- pip 9.0.1
- requests 2.18.4
- unicodecsv 0.14.1

# Methods

MethodName | Description
-|-
get_session_list() | get session list through PyeongChang API
get_session_info(session_code) | get session details of certain session through PyeongChang API
get_price_list(session_code) | get price detail of tickets of certain session through PyeongChang APi
get_session_info_row(session_info) | convert session detail dictinary to array
get_price_list_row(price_list) | convert price detail dictianry to array

# Author

- paht7inder

# Documents

## PyeonChang Project

- [Ch.01. About Project](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-1%EB%B6%80)
- [Ch.02. Enviroment Settings](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EB%8F%99%EA%B3%84-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-2%EB%B6%80)
- [Ch.03. WebSite Analysis](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EB%8F%99%EA%B3%84-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-3%EB%B6%80)
- [Ch.04. Get Session List](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EB%8F%99%EA%B3%84-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-4%EB%B6%80)
- [Ch.05. Get Session Detail](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EB%8F%99%EA%B3%84-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-5%EB%B6%80)
- [Ch.06. Get Price Detail](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EB%8F%99%EA%B3%84-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-6%EB%B6%80)
- [Ch.07. Save CSV file](http://pflb.tistory.com/entry/%ED%8F%89%EC%B0%BD-%EB%8F%99%EA%B3%84-%EC%98%AC%EB%A6%BC%ED%94%BD-%EC%9E%85%EC%9E%A5%EA%B6%8C-%EC%B0%BE%EA%B8%B0-7%EB%B6%80)
