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


# パスワードが正しいかを検証する
def password_verify(password, hash):
    b = base64.b64decode(hash)
    salt, digest_v = b[:16], b[16:]
    digest_n = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),
                                   salt, 10000)
    return digest_n == digest_v


# データベースにユーザーを追加
def add_user(form):
    user_name = form.get('user_name')
    pw = password_hash(form.get('pw'))
    user_id = exec('INSERT INTO users (user_name, password) VALUES(?, ?)',
                   user_name, pw)
    return user_id


# ユーザーネームに該当するユーザーの情報を得る
def get_userid(user_name):
    a = select('SELECT * FROM users WHERE user_name=?', user_name)
    if len(a) == 0:
        return None
    return a[0]


# ユーザーネームからパスワードを得る
def get_password(user_name):
    a = get_userid(user_name)
    return a['password']


# フォームから情報を読み取りチェック、クリアしたらそのままログイン
def judge_login(form):
    user_name = form.get('user_name', '')
    pw = form.get('pw', '')
    if (user_name == '') or (pw == ''):
        msg = 'ユーザーIDもしくはパスワードが入力されていません'
        return False, msg
    a = get_userid(user_name)
    if a is None:
        msg = '入力されたユーザーIDは存在しません'
        return False, msg
    if not password_verify(pw, get_password(user_name)):
        msg = 'ユーザーIDもしくはパスワードが違います'
        return False, msg
    msg = None
    session['login'] = user_name
    return True, msg


# ログアウト処理
def try_logout():
    session.pop('login', None)


# ユーザー名を得る
def get_id():
    return session['login'] if is_login() else '未ログイン'


# ログイン必須を処理するデコレーター
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
