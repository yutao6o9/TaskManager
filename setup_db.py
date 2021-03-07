# データベースを初期化するためだけのモジュール
from summarized_sqlite import exec

exec('''
CREATE TABLE users (
    user_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name  TEXT,
    nickname   TEXT,
    password   TEXT,
    profile    TEXT,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE relations (
    relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    follow_id   INTEGER, /* フォローした人 */
    followed_id INTEGER, /* フォローされた人 */
    created_at  TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE works (
    work_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    created_who  INTEGER,
    type INTEGER DEFAULT 0,
    created_at   TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE routines (
    routine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    works_id   INTEGER,
    title      TEXT,
    memo       TEXT,
    status     INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    works_id   INTEGER,
    title      TEXT,
    memo       TEXT,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE affiliations (
    affiliation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id        INTEGER, /* 誰が */
    project_id     INTEGER, /* どのプロジェクトに */
    created_at     TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE tasks (
    task_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    works_id   INTEGER,
    title      TEXT,
    memo       TEXT,
    in_charge  INTEGER, /* 誰が担当か */
    tag_id     INTEGER,
    deadline   TEXT,
    status     INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')

exec('''
CREATE TABLE tags (
    tag_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id    INTEGER, /* どのタスクについているか */
    name       TEXT,
    created_at TIMESTAMP DEFAULT (DATETIME('now'), ('localtime'))
)
''')
