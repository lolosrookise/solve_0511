a=input()
b=a.split(' ')
c=0
while c!=-1:
    c=0
    for i in range(len(b)-1, 0, -1):
        if len(b)>=1 and b[i] == b[i-1]:
            b.pop(i)
            b.pop(i-1)
            c+=1
            break
    if c == 0:
        c=-1

if len(b) < 1:
    print(1)

else:
    print(0)

