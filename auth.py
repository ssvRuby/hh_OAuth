from hh_const import *
import webbrowser
import socket

import json
import urllib3
import certifi
import requests
from datetime import date, datetime, timedelta
import time

# ----------------------------------------
# Получение кода авторизации пользователя
# ________________________________________

def get_code_for_users_token(code_fut=''):

    webbrowser.open_new_tab(USER_AUTH_PARAMS)

    sock = socket.socket()
    sock.bind((URI, PORT))
    sock.listen(1)

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        code_fut = data.decode('utf-8').split(' ')[1][7:]
        break

    conn.close()
    return code_fut


code_for_users_token = get_code_for_users_token()
print(code_for_users_token)


#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

# Получение токена пользователя (user_access_token)

r = http.request('POST', 'https://hh.ru/oauth/token',
                  headers = {'Content-Type'  : 'application/x-www-form-urlencoded',
                                   'Accept' : '*/*',
                                   'User-Agent' : 'CIO_jbSearch/1.0 (ssv.ruby@gmail.com)'},
                  body  = 'grant_type=authorization_code&client_id={}&client_secret={}&redirect_uri={}&code={}'.format(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, code_for_users_token)
                 )

print(r.data)

user_token_params = json.loads(r.data)

user_token_params['client_id'] = CLIENT_ID
user_token_params['client_secret'] = CLIENT_SECRET
user_token_params['application_token'] = APPLICATION_TOKEN


with open('user_token_params.json', 'w', encoding='utf-8') as f:
    json.dump(user_token_params, f, ensure_ascii=False, indent=4)
