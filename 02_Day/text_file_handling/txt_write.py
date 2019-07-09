#열기모드
#r : 읽기 , w: 쓰기(write - 오버라이트 덮어써짐),  a: 추가(append)
f = open('ssafy.txt', 'w' )

for i in range(10) :
    f.write(f'This is line {i + 1} \n')

f.close()

with open('with_ssafy.txt', 'w') as f: # 컨텍스트 매니저 (코드블럭을 생성 -> 안에서 벗어나면 close를 하지않아도 알아서 종료가 되도록 해줌) , 연파일 을 f라고하겠다. with로하면 할당이불가능함
    for i in range(10) :
        f.write(f'This is line {i + 1} \n')


with open('ssafy.txt', 'w', encoding='utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n']) #한번에 여러가지 텍스트를 적게해줌