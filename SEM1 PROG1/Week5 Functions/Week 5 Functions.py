def my_function():
    print("hello")

my_function()

# passing parameters
def my_function_name(fname):
    print("hello", fname)

my_function_name("Alan")

# overwriting vars
def overwrite(x): # as variable passed in, it will overwrite the global variable
    x[0]=20

lst = [10,22,12,23,23]
overwrite(lst)
print(lst)

# Default params
def functionExample(name, age = 20):
    print("Name: ",name,"\nage:",age)

functionExample("alan")
functionExample("alan",30)

# non sensitive order of params
functionExample(age = 40,name="alan")