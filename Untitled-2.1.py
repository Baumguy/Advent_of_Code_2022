with open("C:/Users/baumb/OneDrive/Desktop/ae27ff/Advent_of_Code/2/input.txt") as f:
    list = f.read().splitlines()
    

P=0
    
for i in list:
    if i[0] == 'A':
        if i[2] == 'X':
            P=P+3
        if i[2] == 'Y':
            P=P+4
        if i[2] == 'Z':
            P=P+8
    if i[0] == 'B':
        if i[2] == 'X':
            P=P+1
        if i[2] == 'Y':
            P=P+5
        if i[2] == 'Z':
            P=P+9
    if i[0] == 'C':
        if i[2] == 'X':
            P=P+2
        if i[2] == 'Y':
            P=P+6
        if i[2] == 'Z':
            P=P+7
    
    print(P)