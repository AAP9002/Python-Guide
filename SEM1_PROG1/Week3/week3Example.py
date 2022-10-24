from pydoc import doc
from re import M


x, y = 3, 5 # initializing multiple variable in one line

if (x > y):
    print(x)
elif x < y: # brackets are optional in python
    print(y)
else:
    print("Equal")

# recommended dont go more than 3 indents deep

## Lists
myList = [['a','b'],[2],[3]]

print(myList[0])
print(myList[0][1])
print(myList[1])

## Dictionary

myDictionary={
    "name":"Alan",
    "age":20,
    "weight":68
    }

print(myDictionary)
print(myDictionary.get("name"))

myDictionary["name"] = "Alan P"
print(myDictionary.get("name"))

newAge = input("What is your new age?")
myDictionary["age"] = int(newAge)

print(myDictionary)