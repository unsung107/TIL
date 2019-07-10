inpu = input().replace(' ','')
words = inpu.split(',')

def chang(a,b):
    for i in range(min(len(a),len(b))) :
        if a[i] > b[i] :
         
            return b,a
            break
        
        elif a[i] < b[i]:
            
            return a,b
            break

for i in range(len(words)-1,0,-1) :
    (words[i-1],words[i]) = chang(words[i-1],words[i])

for i in range(0,len(words)-1) :
    (words[i],words[i+1]) = chang(words[i],words[i+1])

for i in range(len(words)-1):
    print(f'{words[i]}, ', end='')

print(f'{words[i+1]}')
