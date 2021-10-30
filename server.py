from ctypes import string_at
import socket
import datetime
import time

def forsend(string):
    return((bytes(str(string), encoding = 'UTF-8')))

start_time = time.time()
now = datetime.datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 55000))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(10)  # указываем сколько может сокет принимать соединений
print('Сервер запущен')
while True:
    conn, addr = sock.accept()  # начинаем принимать соединения
    print('connected:', addr)  # выводим информацию о подключении
    data = conn.recv(16384)  # принимаем данные от клиента, по 16384 байт
    data = str(data)
    if 'time' in data:
        time = f'Current date: {now.strftime("%d-%m-%Y %H:%M")}'
        conn.send(forsend(time))
        conn.close()
    elif 'up' in data:
        endtime = time.time()
        uptime = f'Uptime: {endtime - start_time}'
        conn.send(forsend(uptime))
        conn.close()

conn.close()  # закрываем соединения