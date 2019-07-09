f = open('ssafy.txt', 'r')
all_text = f.read() # all text 전체를 불러온다. (개행문자포함)
print(all_text)
f.close()

with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)

with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines :
        print(line.strip()) #개행문자제거(print 자체에 개행문자)

with open('ssafy.txt', 'r') as f:
    lines = f.readlines()
    lines.reverse()
    print(lines)
    
    with open('reversed_ssafy.txt', 'w') as d:
        d.writelines(lines)
