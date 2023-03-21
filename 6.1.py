with open("C:/Users/baumb/OneDrive/Desktop/ae27ff/Advent_of_Code/6/6 input.txt") as f:
    input=f.read()

a=4
y=0
z=4
for x in input:
    segment=(input[y:z])
    #print(segment)
    length="".join(set(segment))
    #print(len(length))
    if len(length)==4:
        print(a)
        break
#    for char in segment:
#        p=""
#        if char not in p:
#            p=p+char
#            print(p)
#            if len(p)!=4:
#                print(a)
#                break
    #print(len(p))
    a=a+1
    y=y+1
    z=z+1


 


