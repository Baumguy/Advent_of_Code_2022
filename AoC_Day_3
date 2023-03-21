with open("C:/Users/baumb/OneDrive/Desktop/ae27ff/Advent_of_Code/3/input.txt") as f:
    list = f.read().splitlines()

    m=0

for x in list:
    y=len(x)
    z=int(len(x)/2)
    a=x[:z]
    b=x[z:y]
    #print(a,' ',b)
    s = set(a)
    t = set(b)
    repeats = s&t
    repeats = str(repeats)
    repeats=repeats[2]
    #print(repeats)
    repeats=ord(repeats)
    if repeats > 96:
        m=m+(repeats-96)
    if repeats < 96:
        m=m+(repeats-38)
    #print(repeats)
   # print(m)
print(m)
            
