# import validate_module
import validate_module as vm
# from validate_module import *  ## import * imports all in same name space
while True:
    user_input = input("Enter an integer: ")
    if(not validate_module.is_integer(user_input)):
        print("not an integer")
        continue
    break

#help(validate_module)
#help(validate_module.is_integer)
#print(dir(validate_module))