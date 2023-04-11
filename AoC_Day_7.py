with open("C:/Users/baumb/OneDrive/Desktop/ae27ff/Advent_of_Code/7/7 input.txt") as f:
    input=f.readlines()
    #print(input)

#Defines our variables and dictionaries
Totals = 0
path="/home"
dirs = {"/home":0}

for line in input:
    #resets path if we go back to home directory
    if line == '$ cd /\n':
        path="/home"
    #removes latest directory if we go back a directory
    if line == "$ cd ..\n":
        path = path[:path.rfind("/")]

    #adds to the path dictionary if we're moving deeper into a directory
    if line[:4] == "$ cd" and line.split(' ')[2] != "..\n" and line.split(' ')[2] != "/\n" :
        dir = (line.split(' ')[2][:-1])
        path = path + '/' + dir
        dirs.update({path:0})



    #Finds the size of files in a directory
    if ord('0')<=ord(line[0])<=ord('9'):
        size = (int(line.split(' ')[0]))
        dir = path
        #Adds that size to a dictionary, and adds it to all dictionaries that it's within
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]

#print(dirs)

# === Part One
'''for dir in dirs:
    print(dir, dirs[dir])
    if dirs[dir] <= 100000:
        Totals += dirs[dir]
print("The answer to Part 1 is",Totals)'''

# === Part Two
# I need to remove 9199225 bytes of space.
for dir in dirs:
    if dirs[dir] >=9199225:
        freespace = dirs[dir]
    if dirs[dir] >= 9199225 and dirs[dir] < freespace:
        freespace = dirs[dir]

print("The answer to part two is:", freespace)
