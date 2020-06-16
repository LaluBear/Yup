num = int(input())
Spiral = {}
for i in range(num):
    a,b,c,d = input().split(', ')
    d = d.split(':')
    d = int(d[0])*60+int(d[1])
    if(c not in Spiral):
        Spiral[c] = int(d)
    else:
        Spiral[c] += int(d)
spiral = []            
for i in Spiral:
    spiral.append([Spiral[i],i])
spiral.sort()
spiral = spiral[::-1]
spiral = spiral[:3]
for a,b in spiral:
    a = str(a//60)+":"+str(a%60)
    print(f"{b} --> {a}")
