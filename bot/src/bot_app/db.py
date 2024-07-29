import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("select * from users where user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, lang):
        with self.connection:
            return self.cursor.execute("insert into users (user_id, lang) values (?,?)", (user_id, lang,))
    
    def get_lang(self, user_id):
        with self.connection:
            return self.cursor.execute("select lang from users where user_id = ?", (user_id,)).fetchone()[0]
    
    def update_lang(self, user_id, lang):
        with self.connection:
            return self.cursor.execute("UPDATE users SET lang = ? WHERE user_id = ?", (lang, user_id,))
    
    def get_users(self):
        with self.connection:
            return self.cursor.execute("select user_id from users").fetchall()
            