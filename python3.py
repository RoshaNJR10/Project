#Wap to calculate factorial of given number:
"""
a=int(input("Enter the number to find factorial"))
f=1
for i in range(1,a+1):
    f=f*i
print('the factorial of {} is {}:'.format(a,f))

"""

#Wap to generate the fibonacci Series of nth term:
"""
n=int(input("Enter the term for fibonacci series:"))
a=0
c=0
b=1
print('the {}th fibonacii series are:'.format(n))
for i in range(1,n+1):
    c=a+c
    print(c)
    a=b
    b=c

"""

#Wap to check the given number is prime or composite:
"""
a=int(input("enter the number:"))
for i in range(2,a+1):
    if (a%i==0):
        break
if(a==i):
    print('{} is prime number'.format(a))
else:
    print('{} is composite number'.format(a))

OR,
    c=0
    for i in range (2,a//2):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print("prime")
    else:
        print("composite")

"""

#Wap to print the  prime from range:
"""
a=int(input("enter the lower range for prime"))
b=int(input("Enter the upper range"))

for i in range(a,b+1):
    for j in range(2,b+1):
        if (i%j==0):
            break            
    if(i==j):    
        print(i)

"""
        
#Wap to find the reverse of the given number:
"""
s=0
b=int(input("Enter the number to reverse"))
a=b
while(a!=0):
    r=a%10
    a=a//10
    s=s*10+r
print('the reverse of {} is {}:'.format(b,s))

"""


#Wap to check palindrome:

s=0
b=int(input("Enter the number to reverse"))
a=b
while(a!=0):
    r=a%10
    a=a//10
    s=s*10+r
print('the reverse of {} is {}:'.format(b,s))
if(b==s):
    print("The number is palindrome")
else:
    print("The number is not palindreme")