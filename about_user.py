# ---ユーザー登録、ログインに関する処理をまとめる--- #

import os
import hashlib  # パスワードをハッシュ化するためのモジュール
import base64  # エンコード、デコードするためのモジュール
from functools import wraps

from flask import Flask, session, redirect
from summarized_sqlite import exec, select


# ログインしているかの確認
def is_login():
    return 'login' in session


# 登録のフォーム記入に不備がないかのチェック
def judge_signup(form):
    user_name = form.get('user_name', '')
    pw = form.get('pw', '')
    pw_con = form.get('pw_con', '')
    if user_name == '':
        msg = 'ユーザーIDの欄が空白です'
        return False, msg
    if not check_username(user_name):
        msg = 'このユーザーIDはすでに使われています'
        return False, msg
    if (pw == '') or (pw_con == ''):
        msg = 'パスワードの欄が空白です'
        return False, msg
    if not pw == pw_con:
        msg = 'パスワードの確認が一致していません'
        return False, msg
    msg = None
    return True, msg


# ユーザーネームに重複がないかチェックする
def check_username(user_name):
    a = select('SELECT * FROM users WHERE user_name=?', user_name)
    if len(a) != 0:
        return False
    return True


# パスワードからハッシュを作成する
def password_hash(password):
    salt = os.urandam(16)
    digest = hashlib.pbkdf2_hmac('sha256',
                                 password.encode('utf-8'), salt, 10000)
    return base64.b64encode(salt + digest).decode('ascii')


# データベースにユーザーを追加
def add_user(form):
    user_name = form.get('user_name')
    pw = password_hash(form.get('pw'))
    user_id = exec('INSERT INTO users (user_name, password) VALUES(?, ?)',
                   user_name, pw)
    return user_id


# ログイン必須を処理するデコレーター
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
