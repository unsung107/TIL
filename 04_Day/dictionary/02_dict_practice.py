# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
a1 = sum(score.values())/len(score)
print(int(a1))

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
b1 = 0 ; b2 = 0
for v in scores.keys():
    b1 += sum(scores[v].values())
    b2 += len(scores[v])
print(b1/b2)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.



print('==== Q3-1 ====')
c1 = {}
for v in city.keys() :
    c1[v] = round(sum(city[v])/len(city[v]),2)

for k in c1.keys() :
    print(f'{k} : {c1[k]}')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

d1 = []
for k in city.keys() :
    d1 += city[k]

maxo = max(d1) ; mino = min(d1)

for k in city.keys():
    if maxo in city[k] :
        print(f'가장 더웠던 곳 : {k}')
    
    if mino in city[k] :
        print(f'가장 추웠던 곳 : {k}') 

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

i = 0
for k in city['서울'] :
    if k == 2 :
        i += 1

if i == 0 :
    print('서울은 영상 2도였던 적이 없습니다.')

else :
    print('서울은 영상 2도였던 적이 있습니다.')
    