#no argument and return type:
"""
def sum():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The sum of {} and {} is {}'.format(a,b,a+b))
print("The example of function is:")
sum()
"""
#argument with  no return
"""
def sum(c):
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The sum of {}, {} and {} is {}'.format(a,b,c,a+b+c))
x=int(input("Eneter the value of x:"))
sum(x)
"""
#no argument with return type
"""
def sum():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    return a+b
    print("the sum is:")
print("The sum of a and b is:",sum())
"""
#argument and return type:
"""
def sum(w):
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    return a+b+w
x=sum(5)
print("The sum of a and b is:",x)
"""
"""
def sum(w,x):
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    return a+b+w+x
x=sum(5, 100)
print("The sum of a and b is:",x)
"""

# 1.multiply three number (no argument but return):
"""
def mul():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    c=int(input("Enter the value of c:"))
    return a*b*c
mul=mul()
print("The multiplication of three number  is:",mul)
"""
# 2.multiplication table [argument but no return]:
"""
def mul(a):
    
    for i in range(1,11):
            print('{} x {} = {}'.format(a,i,a*i))
a=int(input("Eneter the value of a:"))

mul(a)
"""


"""
def mul(a,b):
    
    for a in range(1,11):
        for b in range (1,11):
            print('{} x {} = {}'.format(a,b,a*b))
        print("\n")
a=int(input("Eneter the value of a:"))
b=int(input("Enter the value of b:"))
mul(a,b)
"""

# 3.Check odd or even[ no agru no return]
"""
def check():
    a=int(input("Eneter the value of a:"))
    if a%2==0:
        print("Even")
    else:
        print("odd")
check()

"""

# 4.Summ of  1 to n[ argu and return]:
"""
def sum(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
n=int(input("Eneter the value of a:"))
print("The sum is:",sum(n))
"""

def sum():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The sum of {} and {} is {}'.format(a,b,a+b))


def diff():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The diff of {} and {} is {}'.format(a,b,a-b))


def mul():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The mul of {} and {} is {}'.format(a,b,a*b))

def div():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The div of {} and {} is {}'.format(a,b,a/b))
message="1 to continue and other to break"
r=1
while r==1:
    ch=int(input("Enter your choice from 1 to 4:"))
    if ch==1:
        sum()
        r=int(input(message))
    elif ch==2:
        diff()
        r=int(input(message))
    elif ch==3:
        mul()
        r=int(input(message))
    elif ch==4:
        div()
        r=int(input(message))
    else:
        print("Invalid Choice")
        r=int(input(message))