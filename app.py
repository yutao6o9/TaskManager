from flask import Flask, render_template, redirect, request

import about_user as user

app = Flask(__name__)
app.secret_key = 'dIfk2EV4Ds7odVWK'


@app.route('/signup')
def signup():
    return render_template('signup_form.html')


@app.route('/signup/try', methods=['POST'])
def try_signup():
    judge, msg = user.judge_signup(request.form)
    if not judge:
        return redirect('/signup', msg=msg)
    return redirect('/user/<user_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
