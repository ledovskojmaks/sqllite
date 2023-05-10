import datetime
import socket
from db import BotDB

BotDB = BotDB('user_db.db')

# Функция для получения текущей временной метки
def get_current_timestamp():
    return datetime.datetime.now()

# Функция для получения IP-адреса пользователя
def get_user_ip():
    return socket.gethostbyname(socket.gethostname())

def push_data(event_name, is_authorized):
    user_ip = get_user_ip()
    timestamp = get_current_timestamp()
    BotDB.add_data(event_name, is_authorized, user_ip, timestamp)



if __name__ == "__main__":
    
