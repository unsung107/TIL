from flask import Flask, render_template
import datetime 
import random
app = Flask(__name__)

@app.route("/") # endpoint
def hello():
    return render_template('index.html')


@app.route("/ssafy")
def ssafy():
    return 'hello keeeff'


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 10, 22)
    td = b_day - today
    return f'{td.days}일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>This is html h1 tag</h1>'


@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>

    '''


#variable routing
@app.route('/greeting/<name>')
def greeting(name):
    return render_template('greeting.html', html_name=name) #이 네임을 안에있는 html에서 html_name이라는 걸로 쓸수있도록 넘겨줌


@app.route('/cube/<int:number>')
def cube(number):
    return render_template('cube.html', html_num=number, html_result=number ** 3)


#실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = []
    for i in range(people+5):
        menu.append(f'라면 중 {i} 번째로 맛있는 라면')
    order = random.sample(menu, people)

    return str(order)
    

@app.route('/movie')
def movie():
    movies = ['스파이더맨파프롬홈' , '어벤져스앤드게임' , '기생충' , '알라딘']
    return render_template('movie.html', movies=movies)

if __name__ == '__main__': #app.py 가 직접 실행되었을때만 !

    app.run(debug=True)
