from hh_const import *

import webbrowser
import socket
from threading import Thread


### Получение авторизации пользователя
#def w_open():
#    webbrowser.open_new_tab(USER_AUTH_PARAMS)

def get_code_for_users_token(code_fut=''):
    def w_open():
        webbrowser.open_new_tab(USER_AUTH_PARAMS)


    sock = socket.socket()
    sock.bind((URI, PORT))
    sock.listen(1)

    w_thread = Thread(target=w_open)
    w_thread.start()

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        code_fut = data.decode('utf-8').split(' ')[1][7:]
        conn.close()
        w_thread._delete()
        break

    return code_fut


code_for_users_token = get_code_for_users_token()
print(code_for_users_token)