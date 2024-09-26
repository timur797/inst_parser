import instaloader
import sqlite3

USER = ""
PWD = ""

conn = sqlite3.connect('followers.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS followers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL
)
''')

il = instaloader.Instaloader()
il.login(user=USER, passwd=PWD)
username = 'skillbox.ru'
profile = instaloader.Profile.from_username(il.context, username=username)


for follower in profile.get_followers()[:50]:
    cursor.execute('INSERT INTO followers (username) VALUES (?)', (follower.username,))

conn.commit()
conn.close()
