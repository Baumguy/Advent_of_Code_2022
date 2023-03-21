with open("C:/Users/baumb/OneDrive/Desktop/ae27ff/Advent_of_Code/4/input.txt") as f:
    list = f.read().splitlines()

z=0    

for x in list:
    #print(x)
    y=x.split(',')
    #print(y)
    m,n=y
    #print(m,n)
    o,p=m.split('-')
    q,r=n.split('-')
    o=int(o)
    p=int(p)
    q=int(q)
    r=int(r)
    a=range(o,p+1)
    b=range(q,r+1)
    #print(a,b)
    a=set(a)
    b=set(b)
    #print(a,b)
    c=a.intersection(b)
    if c != set():
        z=z+1

print(z)
    

    