from flask import Flask, render_template, request #사용자의 요청을 확인할 수 있음
import requests
import bs4

app = Flask(__name__)

# www.google.com[/serch]
@app.route('/') # / -> root
def index():
    return 'Hello World ~_~'


@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age') #사용자가 보낸 값들 중 'age'를 꺼내겠다
    return f'Pong! age = {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('/ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    #Ascii art aip 를 활용하여 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    print(result)
    return render_template('ascii_result.html', result=result)


if __name__ == '__main__': #app.py 가 직접 실행되었을때만 !
    app.run(debug=True)
