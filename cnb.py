import random
l1=[]
a=random.randint(1,9)
b=random.randint(0,9)
while(b==a):
    b=random.randint(0,9)
c=random.randint(0,9)
while(c==b or c==a):
    c=random.randint(0,9)
d=random.randint(0,9)
while(d==c or d==b or d==a):
    d=random.randint(0,9)
l1.append(str(a))
l1.append(str(b))
l1.append(str(c))
l1.append(str(d))
z=0
    
while(1):
    z=z+1
    print("enter a number :")
    s=input()
    l2=list(s)
    bull=0
    cow=0
    for x in range(0,4):
        if(l2[x]==l1[x]):
            bull=bull+1
    for x in range(0,4):
        for y in range(0,4):
            if(l1[x]==l2[y] and x!=y):
                cow=cow+1
                break
    print(bull,"bull",end=" ")
    print(cow,"cow")
    if(bull==4):
        print("u got it right in",z,"steps")
        break
