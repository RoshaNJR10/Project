# to find min,max,sum,average
data=list(map(int,input("ENter the data").split(",")))
print(data)

message="1 to continue other to break"
r=1
while(r==1):
    ch=int(input("enter choice 1-4:"))
    if(ch==1):
        print(min(data))
        r=int(input(message))
        
    elif(ch==2):
        print(max(data))
        r=int(input(message))
    elif(ch==3):
        print(sum(data))
        r=int(input(message))
    elif(ch==4):
        print("Average=",(sum(data)/len(data)))
        r=int(input(message))
    else:
        print("try again")
        r=int(input(message))