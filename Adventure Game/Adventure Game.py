### Adventure game - Alan Prophett ###
import time,os

#loading screen
print("Loading . . . . . . .")
time.sleep(2)

playerSettings = {
	"name" : os.getlogin(),
	"characterName" : "",
	"characterAge" : 520

}

#intro and name
print("Welcome to my Adventure Game", os.getlogin(),"!",'\n',"Choose your character:")

#choose you character
characterList = ["Knight","Warrior","Wizard"]#list of character types

# i=0
# while i<len(characterList):
#     print(str(i+1)+". "+characterList[i])
#     i+=1

for idx, val in enumerate(characterList,start=1):
	print(str(idx)+ ". "+ val)

playerSettings["characterName"] = characterList[int(input("Type in your character number:"))-1]
print("you chose: " +playerSettings.get("characterName"))


settingsMenu = ["Player name","Character name","Character age", "View Current Settings"]

while True:
	menu = int(input("Would you like to (1) start or (2) change settings?"))

	if menu ==1:
		move = input("\n "+ playerSettings.get("characterName")+", do you want to move?")
		count =0
		while move in ('Yes','yes','Y','y'):
			print("You've moved 1 space")
			move = input(playerSettings.get("characterName")+", keep moving?")
		else:
			print("You moved "+count+" spaces")
			break
	elif menu ==2:
		for idx, val in enumerate(settingsMenu,start=1):
			print(str(idx)+ ". "+ val)
		settingChange = int(input("What would you like the change?"))

		if settingChange == 1:
			playerSettings["name"] = input()
			print("changed")
		elif settingChange == 2:
			playerSettings["characterName"] = input()
			print("changed")
		elif settingChange == 3:
			playerSettings["characterAge"] = input()
			print("changed")
		elif settingChange == 4:
			print(playerSettings)
	else:
		print("INVALID")


input("PRESS ANY KEY TO EXIT")# pause before terminating