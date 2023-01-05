#Wapt to create greatest among three three numbers:
"""
a=int(input("Entr 1st num:"))
b=int(input("Entr 1st num:"))
c=int(input("Entr 1st num:"))
if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is greatest")
else:
    print("c is greatest")
"""
#calculate add sub mul and div acc to usser need:

"""
r=1
while(r==1):
    a=float(input("Entr 1st num:"))
    b=float(input("Entr 1st num:"))
    print("Enter 1 for add:\nEnter 2 for diff:\nEnter 3 for mul:\nEnter 4 for div:\n")
    ch=int(input("enter choice from 1 to 4: "))
    
    if ch==1:
        print("the sum of a and b is:",a+b)
        r=int(input("enter 1 for continue else break"))
    elif ch==2:
        print("the diff of a and b is:",a-b)
        r=int(input("enter 1 for continue else break"))
    elif ch==3:
        print("the mul of a and b is:",a*b)
        r=int(input("enter 1 for continue else break"))
    elif ch==4:
        print("the div of a and b is:",a/b)
        r=int(input("enter 1 for continue else break"))
    else:
        print("enter valid chooice:")
        r=int(input("enter 1 for continue else break"))
"""

#Multiplication table:
"""
for i in range(1,11):
    for j in range(1,11):
        print("{}x{}={}".format(i,j,i*j))
    print("\n")
    """

#cube of given num
"""
a=float(input("Entr number for cube:"))
print("cube is:",a**3)
"""

#even num in given range:
"""
a=int(input("Entr lower range:"))
b=int(input("Entr upper num:"))
for i in range(a,b):
    if(i%2==0):
        print(i)
        """
    
#csldulate factorial:
"""
a=int(input("Entr num for factorial:"))
f=1
for i in range(1,a+1):
    f=f*i
print(f)
"""

#fibonacci series:
"""
n=int(input("Entr num of terms:"))
a=0
b=0
c=1

for i in range(1,n+1):
    print(a)
    
    b=c
    c=a
    a=b+c
"""

#prime or composite:
"""
n=int(input("Entr num of terms:"))
for i in range(2,n+1):
    if(n%i==0):
     break
if(n==i):
    print("p")
else:
    print("c")

    """

#reverse
"""
n=int(input("Entr num :"))
rev=0
while(n!=0):
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)
"""

#Prime in range
"""
a=int(input("Entr num of terms:"))
b=int(input("Entr num of terms:"))
for i in range(a,b+1):
    for j in range(2,b+1):
        if(i%j==0):
            break
    if(i==j):
        print(i)
  """

#palindrome:
"""
n=int(input("Entr num :"))
a=n
rev=0
while(n!=0):
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)
if a==rev:
    print("p")
else:
    print("n")
"""

#list
#create and print list
q=["arm","ram","mar"]
"""
print(q)
for f in q:
     print(f,end="/")
"""
#insert in end of list
li=list(map(str,input("Enter number").split()))#split tells the way to insert element

print(li)
"""
app=input("Enter value to insert:")
li.append(app)
print(li)
"""
#insert at specific position

n=int(input("Enter index"))
"""
li.insert(n,"hari")
print(li)
"""
# delete data from index
"""
del li[n]
print(li)"""
#remove data
li.remove("ram")
print(li)

