words = input().split(',')

def chang(a=[],b=[]):
    for i in range(min(len(a),len(b))) :
        if a[i] > b[i] :
         
            return(b,a)
        
        elif a[i] < b[i]:
            
            break

a = 'list'
b = 'copy'
print(a[0]>b[0])
(a,b) = chang(a,b)

print(a[0]>b[0])
print(a)
print(b)

