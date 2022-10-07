from hh_const import *
import webbrowser
import socket

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