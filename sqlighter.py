import sqlite3

class sqlighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    def add_subscriber(self, user_id, happy=0, unhappy=0, marry=0,sorry=0,angry=0,sad=0,cheerful=0,high_spirited=0,low_spirited=0):
        with self.connection:
            return self.cursor.execute("INSERT INTO `list` (`user_id`, `happy`, `unhappy`,`marry`, `sorry`, `angry`,`sad`,`cheerful`, `high_spirited`, `low_spirited`) VALUES(?,?,?,?,?,?,?,?,?,?)", (user_id,happy,unhappy,marry,sorry,angry,sad,cheerful,high_spirited,low_spirited))

    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `list` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))
        # получаем все занчения из таблицы
    def get_data(self,user_id):
        mooddata = self.cursor.execute('SELECT * FROM `list` WHERE `user_id` = ?', (user_id,)).fetchall()
        return mooddata

    def mood_update(self,mood_name,score,user_id):
        self.cursor.execute(f'UPDATE `list` SET {mood_name} = ? WHERE `user_id` = ?', (score,user_id,) )
        #self.cursor.execute('UPDATE `list` SET `happy` = ? WHERE `user_id` = ?', (happy,user_id,) )
        self.connection.commit()

    def close(self):
        self.connection.close()