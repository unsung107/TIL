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

@app.route('/lotto_input')
def lotto_input():
    #사용자가 입력할 수 있는 페이지만 전달
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    lotto_numbers = request.args.get('numbers').split(' ')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() #json 타입의 파일을 python dictionary 로 parsing 해줘
    mine = set(lotto_numbers)
    before = []
    bonus = str(lotto_info['bnusNo'])
    for k in lotto_info.keys():
        if 'drwtNo' in k:
            before.append(str(lotto_info[k]))
    goal = set(before)

    result = mine & goal
    deung = '꽝'
    
    if len(result) == 6:
        deung = '1등'
    elif len(result) == 5:
        if bonus in mine:
            deung = '2등'
        else : deung = '3등'
    elif len(result) == 4:
        deung = '4등'
    elif len(result) == 3:
        deung = '5등'
    
    return f'당신은 {deung}입니다'




if __name__ == '__main__': #app.py 가 직접 실행되었을때만 !
    app.run(debug=True)
