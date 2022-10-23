#Fizz Buzz game
#Fizz if divisible by 3
#Buzz if divisible by 5
#otherwise output the number
#
#numbers are elements of the natural numbers
#from 0 to users input value

def Classify(currentNumber):
    #this function will output "Fizz", "Buzz" or the number
    #:input int currentNumber number to assess
    #:output none

    if currentNumber % 15 == 0:
        print("Fizz Buzz")
    elif currentNumber % 3 == 0:
        print("Fizz")
    elif currentNumber % 5 == 0:
        print("Buzz")
    else:
        print(currentNumber)


number = int(input("0 to what number?\nEnter number:"))

#foreach number from 0 to number
for x in range(number+1): Classify(x)
