print("hello world")

print(1 + 3)
print("1 + 3 = "+ str(1 + 3)) #this is a concatenation of 2 strings
#str will cast to string

message = "Welcome to COMP16321"
print(message)

number = 12.3
print(type(number)) #use type to output the current var type
print(number)

number = "now a string" #naming conventions need to be strict so debugging isn't confusing
print(type(number))
print(number)

#lists
myList = [1,"String",3.33] # you can mix types
print(myList) #output whole list
print(myList[2]) #indexing starts at 0