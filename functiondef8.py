# function defination:
#no return and argument
def add():
    li=list(map(int,input("Enter the data:").split()))
    print(li)
    s=sum(li)
    print("The sum is:",s)


#no argument but return
def diff():
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    s=a-b
    return s
    # print('The diff of {} and {} is {}'.format(a,b,a-b))

#argument but no return
def mul(x):
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    print('The mul of {},{} and {} is {}'.format(a,b,x,a*b*x))

#return type and argument
def div(x):
    a=int(input("Eneter the value of a:"))
    b=int(input("Enter the value of b:"))
    div=a/b/x
    return div

pi=3.14

