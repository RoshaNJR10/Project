# Wap to create and display its element
"""
fr=["rosan","csit","5th","sem","BSC","nist","college"]
print(fr)
#to print individual
for f in fr:
    print(f)
    # to print each word
    for w in f:
        print(w)
#to print individual data in format
for f in fr:
    print(f,end=(""))
"""

# To take input in list and print it
"""
li=list(map(str,input("Enter data:").split()))
print(li)
"""
#to print specific index value and the index of given value
"""
li=["rosan","csit","5th","sem","BSC","nist","college"]
print(li[3])
print(li.index("5th"))
"""

# To perform operation in list:
message="1 for continue other for break"
li=["rosan","csit","5th","sem","BSC","nist","college"]
r=1
while(r==1):
    ch=int(input("ENter your choice 1-6"))
    if(ch==1):
        print(li)
        app=input("enter the value to append")
        li.append(app)
        print("after append:",li)
        r=int(input(message))
        
    elif(ch==2):
        print(li)
        ins=input("Enter the value to insert")
        ind=int(input("enter the index in which to insert"))
        li.insert(ind,ins)
        print("Data after insertion:",li)
        r=int(input(message))
    elif(ch==3):
        print(li)
        ind=int(input("Enter the inddex to delete"))
        del li[ind]
        print("Data after deletion:",li)
        r=int(input(message))
    elif(ch==4):
        print(li)
        dat=input("enter the value to delete")
        li.remove(dat)
        print("Data after remove:",li)
        r=int(input(message))
    elif(ch==5):
        print(li)
        ind=int(input("entre index"))
        li.pop(ind)
        print("Data after pop:",li)
        r=int(input(message))
    elif(ch==6):
        print(li)
        li.clear()
        print(li)
        r=int(input(message))
    else:
        print("wrong input")
        r=int(input(message))
        


