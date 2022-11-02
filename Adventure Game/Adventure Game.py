#--- Adventure game - Alan Prophett ---
import time,os

def overwriteSettings(currentSettings):
        with open("settings.txt",'w') as file:
                for item in currentSettings:
                        file.write("%s\n"%item)

#loading screen
print("Loading . . . . . . .")
time.sleep(1)

playerSettings = list()

# with open("settings.txt") as file:
#        playerSettings = file.readlines()

playerSettings = [line.rstrip('\n') for line in open("settings.txt")]

#intro and name
# os.getlogin()
print("Welcome to my Adventure Game",playerSettings[0] ,"!",'\n',"Choose your character:")

#choose you character
characterList = ["Knight","Warrior","Wizard"]#list of character types

# i=0
# while i<len(characterList):
#     print(str(i+1)+". "+characterList[i])
#     i+=1

for idx, val in enumerate(characterList,start=1):
	print(str(idx)+ ". "+ val)

playerSettings[1] = characterList[int(input("Type in your character number:"))-1]
print("you chose: " +playerSettings[1])
overwriteSettings(playerSettings)


settingsMenu = ["Player name","Character name","Character age", "View Current Settings"]

while True:
	menu = int(input("Would you like to (1) start or (2) change settings?"))

	if menu ==1:
		move = input("\n "+ playerSettings[1]+", do you want to move?")
		count =0
		while move in ('Yes','yes','Y','y'):
			print("You've moved 1 space")
			count+=1
			move = input(playerSettings[1]+", keep moving?")
		else:
			print("You moved "+str(count)+" spaces")
	elif menu ==2:
		for idx, val in enumerate(settingsMenu,start=1):
			print(str(idx)+ ". "+ val)
		settingChange = int(input("What would you like the change?"))

		if settingChange == 1:
			playerSettings[0] = input()
			overwriteSettings(playerSettings)
			print("changed")
		elif settingChange == 2:
			playerSettings[1] = input()
			overwriteSettings(playerSettings)
			print("changed")
		elif settingChange == 3:
			playerSettings[2] = input()
			overwriteSettings(playerSettings)
			print("changed")
		elif settingChange == 4:
			print(playerSettings)
	else:
		print("INVALID")


input("PRESS ANY KEY TO EXIT")# pause before terminating
