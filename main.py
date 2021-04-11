from flask import Flask

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=8080, host='127.0.0.1')
