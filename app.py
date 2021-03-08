from flask import Flask, render_template, redirect

app = Flask(__name__)
app.secret_key = 'dIfk2EV4Ds7odVWK'


@app.route('/signup')
def signup():
    return render_template('signup_form.html')


@app.route('/signup/try', methods=['POST'])
def try_signup():
    return redirect('/user/<user_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
