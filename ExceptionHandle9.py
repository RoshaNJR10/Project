#Error occured
"""
try:
    f=open("ro.txt","r")
    print(f.read())
except NameError:
    print("variable not defined")
except:
    print("Error occured")
"""
#NameError
"""
try:
    print(x)
except NameError:
    print("variable not defined")
except:
    print("Error occured")
    """
#Divide by zero error:
"""
try:
    x=4
    print(x/0)
except ZeroDivisionError:
    print("Divideby zero error")
except NameError:
    print("variable not defined")
    """


