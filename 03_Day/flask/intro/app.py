from flask import Flask
import datetime 
import random
app = Flask(__name__)

@app.route("/") # endpoint
def hello():
    return "Hello SSAFY!"



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
@app.route('/greeting/iu')
def greeting_IU():
    return '반갑습니다! IU님!'
@app.route('/greeting/ziont')
def greeting_ziont():
    return '반갑습니다! ziont님!'
#variable routing
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다! {name} 님!'

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 3 제곱은 {number ** 3} 입니다.'


#실습
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = []
    for i in range(people+5):
        menu.append(f'라면 중 {i} 번째로 맛있는 라면')
    order = random.sample(menu, people)

    return str(order)
    

if __name__ == '__main__': #app.py 가 직접 실행되었을때만 !

    app.run(debug=True)