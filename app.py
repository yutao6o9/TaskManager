from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'dIfk2EV4Ds7odVWK'


@app.route('/signup')
def signup():
    return render_template('signup_form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
