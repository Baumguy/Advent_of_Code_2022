with open('input.txt') as file:
        data = [i for i in file.read().strip().split("\n")]
        
max = 0
count = 0
max2=0
max3= 0
c=0
b=0
for item in data:
        if item == '':
                count = 0
        else:
                num = int(item)
                count += num
        if count > max3:
                max3 = count
        if max3 > max2:
                floater = max2
                max2 = max3
                max3 = floater
        if max2 > max:
            floater = max
            max = max2
            max2 = floater

print(max3)
print(max2)
print(max)
Three_highest=(max3, max2, max)
print(sum(Three_highest))