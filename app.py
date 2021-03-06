from flask import Flask

app = Flask(__name__)
app.secret_key = 'dIfk2EV4Ds7odVWK'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
