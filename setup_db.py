# データベースを初期化するためだけのモジュール
from summarized_sqlite import exec

exec('''
CREATE TABLE users (
    user_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name  TEXT,
    nickname   TEXT,
    email      TEXT,
    password   TEXT,
    profile    TEXT,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')
