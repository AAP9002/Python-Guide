import time, os

time.sleep(2)
print("Done "+os.getlogin())

myList = list(range(1,11,2)) #creates list 1-10 with a step of 2
print(myList)
myList2 = list(range(1,11,1)) #creates list 1-10
print(myList2)

i=0
while i<4:
    print("While: "+str(i))
    i +=1  #i=i+1

for x in range(4):
    print("for: "+str(x))

for x in range(2,13,2):
    print("For Sequence: "+str(x))

fruits = ["apple","banana", "pear"]

for x in fruits:
    print(x)

for x in "banana":
    print(x)

adj = ["ripe", "moldy"]

for x in adj:
    for y in fruits:
        print(x,y)