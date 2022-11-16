"""Add a bunch of functions to validate user input"""

print("module imported")

def is_integer(value):
    """Returns True if the value is an integer, otherwise returns False"""
    try:
        int(value)
        return True
    except:
        return False