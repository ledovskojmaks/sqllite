import sqlite3

class BotDB:

    def __init__(self, user_db):
        """Инициализируем соеденение с БД"""
        self.conn = sqlite3.connect(user_db)
        self.cursor = self.conn.cursor()

    def add_data_users(event_name, is_authorized, user_ip, timestamp):
        """Создаем запись данных события"""
        self.cursor.execute("INSERT INTO 'Data_users' ('event_name', 'is_authorized', 'user_ip', 'timestamp') VALUES(?, ?, ?, ?)",
                            (event_name, is_authorized, user_ip, timestamp))
        return self.conn.commit()
    
    def close(self):
        """Закрытие БД"""
        self.conn.close()
