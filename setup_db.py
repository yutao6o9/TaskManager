# データベースを初期化するためだけのモジュール
from summarized_sqlite import exec

exec('''
CREATE TABLE users (
    user_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name  TEXT,
    password   TEXT,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE works (
    work_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    created_who  INTEGER,
    created_at   TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE tasks (
    task_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    works_id   INTEGER,
    title      TEXT,
    memo       TEXT,
    deadline   TEXT,
    status     INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')
