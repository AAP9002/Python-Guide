import os
#overwrite file
lines = 'Alan\nProphett\n3\n4\n5\n'
f = open("Settings.txt",'w')
f.write(lines)
f.close()


print("#### TEST 1 ####")
f = open("Settings.txt",'r') # read textfile mode
print(f.read(7)) #  read first 7 characters
f.close() # close to reduce use of resources

print("#### TEST 2 ####")
def display(filename):
     f = open(filename,'r')
     lines = f.read() # read All
     print(lines)
     f.close()
display("Settings.txt")

print("#### TEST 3 ####")
f = open("Settings.txt",'r')
for line in f:
     print(line) # output all lines
f.close()

print("#### TEST 4 ####")
f = open("Settings.txt",'a') # add to end (a-> append)
f.write("\nnew text Appended") # add text to end
f.close()
display("Settings.txt")

print("#### TEST 5 ####")
if os.path.isfile("makeAfile.txt"):
     os.remove("makeAfile.txt")
f = open("makeAfile.txt",'x') # add to end (a-> append)
f.write("new file text") # add text to end
f.close()
display("makeAfile.txt")
