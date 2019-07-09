with open('ssafy.txt', 'r') as f:
    lines = f.readlines()
    lines.reverse()
    
with open('reversed_ssafy.txt', 'w') as d:
    d.writelines(lines)
