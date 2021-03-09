# ---ユーザー登録、ログインに関する処理をまとめる--- #

import os
import hashlib  # パスワードをハッシュ化するためのモジュール
import base64  # エンコード、デコードするためのモジュール
from functools import wraps

from flask import Flask, session, redirect


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
    if (pw == '') or (pw_con == ''):
        msg = 'パスワードの欄が空白です'
        return False, msg
    if not pw == pw_con:
        msg = 'パスワードの確認が一致していません'
        return False, msg
    msg = ''
    return True, msg


# パスワードからハッシュを作成する
def password_hash(password):
    salt = os.urandam(16)
    digest = hashlib.pbkdf2_hmac('sha256',
                                 password.encode('utf-8'), salt, 10000)
    return base64.b64encode(salt + digest).decode('ascii')


# ログイン必須を処理するデコレーター
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
