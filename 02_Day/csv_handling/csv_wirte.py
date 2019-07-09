dinner = {
    '양자강' : '02-557-4211' , #차돌짬뽕
    '김밥카페' : '02-553-3181', #라돈
    '순남시래기' : '02-508-0887' #보쌈정식
}

# 1. String formatting
with open('dinner.csv', 'w', encoding="utf-8") as f :
    for item in dinner.items(): #[['양자강', '02-557-4211'],[,],[,]]
        f.write(f'{item[0]},{item[1]}\n') #양자강,02-557-4211

# 2. csv writer 
import csv

with open('dinner.csv', 'w', encoding="utf-8", newline='') as f: #newline -> 윈도우에서는 csv를 import해서 write해서 한줄씩 작성하면 한줄씩 더 작성됨. 그걸 없애기위해서 newline에 빈칸을둠을 권장 #encoding 등 옵션으로 줄때는 =""붙여서주는게 컨벤션
    csv_writer = csv.writer(f) # f라는 파일에 csv를 작성하는 객체를 생성  
    for item in dinner.items():
        csv_writer.writerow(item)