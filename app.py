from flask import Flask, render_template, redirect, request

import about_user as user

app = Flask(__name__)
app.secret_key = 'dIfk2EV4Ds7odVWK'


# --- ログイン関係 --- #
@app.route('/signup')
def signup():
    return render_template('signup_form.html')


@app.route('/signup/try', methods=['POST'])
def try_signup():
    judge, msg = user.judge_signup(request.form)
    if not judge:
        return redirect('/signup', msg=msg)
    user_id = user.add_user(request.form)
    # 登録したらそのままログインに移行したい
    return redirect('/login')


@app.route('/login')
def login():
    return render_template('login_form.html')


@app.route('/login/try', methods=['POST'])
def try_login():
    judge, msg = user.judge_login(request.form)
    if not judge:
        return redirect('/login', msg=msg)
    return redirect('/')
# ----------------------------------------------- #


@app.route('/')
def index():
    return redirect('/signup')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
