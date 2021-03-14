from flask import Flask, render_template, redirect, request

import about_user as user
import about_task as task

app = Flask(__name__)
app.secret_key = 'dIfk2EV4Ds7odVWK'


# --- ログイン関係 --- #
@app.route('/signup')
def signup():
    return render_template('signup_form.html', status=user.is_login())


@app.route('/signup/try', methods=['POST'])
def try_signup():
    judge, msg = user.judge_signup(request.form)
    if not judge:
        return error_msg(msg)
    user_id = user.add_user(request.form)
    # 登録したらそのままログインに移行したい
    return redirect('/login')


@app.route('/login')
def login():
    return render_template('login_form.html', status=user.is_login())


@app.route('/login/try', methods=['POST'])
def try_login():
    judge, msg = user.judge_login(request.form)
    if not judge:
        return error_msg(msg)
    return redirect('/user/' + str(user.get_id()))


@app.route('/logout')
def logout():
    user.try_logout()
    return redirect('/login')
# ----------------------------------------------- #


@app.route('/')
def index():
    status = user.is_login()
    if not status:
        return redirect('/signup')
    return redirect('/user/' + str(user.get_id()))


@app.route('/user/<user_id>')
@user.login_required
def user_page(user_id):
    return render_template('task.html', status=user.is_login(),
                           user_name=user.get_id())


@app.route('/task/try', methods=['POST'])
@user.login_required
def try_add_task():
    task_id, msg = task.add_task(request.form)
    return redirect('/user/' + str(user.get_id()))


def error_msg(msg):
    return render_template('msg.html', msg=msg, status=user.is_login())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
