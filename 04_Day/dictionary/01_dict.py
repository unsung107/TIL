#딕셔너리 만들기
lunch1 = {
    '중국집': '02'
}
print(lunch1)

lunch2 = dict(중국집='02')
print(lunch2)

#딕셔너리 내용 추가하기
lunch1['분식집'] = '031'

#딕셔너리 내용 가져오기

idol = {
    'bit':{
        '지민':24,
        'RM': 25
    }
}
print(idol['bit']['RM'])

#딕셔너리 반복문 활용하기
for key in lunch1 :
    print(key,lunch1[key])

#value key items 기ㅏ져오기

for key, value in lunch1.items() :
    print(key, value)