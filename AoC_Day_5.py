with open("C:/Users/baumb/OneDrive/Desktop/ae27ff/Advent_of_Code/5/input.txt") as f:
    list = f.read().splitlines()


List1=['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P']
List2=['L', 'D', 'Z', 'Q', 'W', 'V']
List3=['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C']
List4=['R', 'D', 'H', 'F', 'J', 'V', 'B']
List5=['Z', 'W', 'L', 'C']
List6=['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M']
List7=['J', 'R', 'L', 'V', 'M', 'B', 'S']
List8=['D', 'P', 'J']
List9=['D', 'C', 'N', 'W', 'V']
ListofLists=[List1, List2, List3, List4, List5, List6, List7, List8, List9]

z=0

for container in list:
    #print(container)
    parts=container.split(' ')
    move=int(parts[1])
    start=int(parts[3])-1
    end=int(parts[5])-1
    #print(ListofLists[start])
    #print(ListofLists[end])
    #print(move,start,end)
    #long=len(ListofLists[start])-1
    #print(long)
    while z < move:
        #looong=long-z
        long=len(ListofLists[start])-1
        #print("Length of start:", len(ListofLists[start]))
        #print("This is long:", long)
        #print("Before:", ListofLists[start])
        #print(ListofLists[start][looong])
        ListofLists[end].append(ListofLists[start][long])
        del(ListofLists[start][long])
        z+=1
        #print("After:", ListofLists[start])
        #print(ListofLists[end])    
        #print(z, "of", move)
    else:
        z=0
        #print("This is the end of a loop")
        
           

#print(ListofLists[start])
#print(ListofLists[end])
print(ListofLists)
print(List1[len(List1)-1], List2[len(List2)-1], List3[len(List3)-1], List4[len(List4)-1], List5[len(List5)-1], List6[len(List6)-1], List7[len(List7)-1], List8[len(List8)-1], List9[len(List9)-1])
