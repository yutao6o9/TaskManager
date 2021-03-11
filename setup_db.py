# データベースを初期化するためだけのモジュール
import sqlite3
from summarized_sqlite import open_db


db = open_db()
c = db.cursor()
c.execute(
    'CREATE TABLE users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, password TEXT)')

c.execute(
    'CREATE TABLE works(work_id INTEGER PRIMARY KEY AUTOINCREMENT, created_who INTEGER)')

c.execute('CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, works_id INTEGER, title TEXT, memo TEXT, deadline TEXT, status INTEGER DEFAULT 0)')

db.commit()
db.close()
