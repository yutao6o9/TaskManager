import os
import sqlite3


# パス
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = BASE_DIR + '/data/app_data.sqlite3'


# データベースを開く
def open_db():
    conn = sqlite3.connect(DATA_DIR)
    conn.row_factory = dict_factory
    return conn


# SELECT句の結果を辞書型で得られるようにする
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# SQLの実行をまとめた関数
def exec(sql, *args):
    db = open_db()  # データベースを開く
    c = db.cursor()  # カーソルを得る
    c.execute(sql, args)  # sqlはSQL文 argsはテーブルの各ラベル
    db.commit()  # コミットで反映
    return c.lastrowid  # 一番最後にINSERTしたやつの識別IDを返す


# SQLを実行して結果を得る
def select(sql, *args):
    db = open_db()
    c = db.cursor
    c.execute(sql, args)
    return c.fetchall()  # SELECT文に該当するデータを全て返す
