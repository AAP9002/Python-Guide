f = open("Settings.txt",'r')

print(f.read(6))


f.close()

f = open("Settings.txt",'r')
for line in f:
     print(line)
f.close()

