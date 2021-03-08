# ---ユーザー登録、ログインに関する処理をまとめる--- #

import hashlib  # パスワードをハッシュ化するためのモジュール
import base64  # エンコード、デコードするためのモジュール
from functools import wraps

from flask import Flask, session, redirect


# ログインしているかの確認
def is_login():
    return 'login' in session


# 登録のフォーム記入に不備がないかのチェック
def get_input(form):
    user_id = form.get('user_name', '')
    pw = form.get('pw', '')
    pw_con = form.get('pw_con', '')
    if user_id == '':
        msg = 'ユーザーIDの欄が空白です'
        return False
    if (pw == '') or (pw_con == ''):
        msg = 'パスワードの欄が空白です'
        return False
    if not pw == pw_con:
        msg = 'パスワードの確認が一致していません'
        return False
    return True


# ログイン必須を処理するデコレーター
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_login:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
