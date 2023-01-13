#create a file
"""
f=open("hello.txt","x")
"""

#Write in existing file
"""
f= open("ros.txt","w")
f.write("My name is roshan.")
f.close()
"""
#Read the existing file
"""
f=open("ros.txt","r")
print(f.read())
"""

#Append in existing file.It adds in existing file:
"""
f=open("ros.txt","a")
f.write("I am from Bhakumde")
f.close()


f=open("ros.txt","r")
print(f.read())
"""

#Writing existing file will replace the previous content.To add append is needed
"""
f=open("ros.txt","w")
f.write("I am from Banepa")
f.close()
f=open("ros.txt","r")
print(f.read())
"""

# delete the file from the path
"""
import os
os.remove("E:\\group-nist-4\\Roshan\\python\\rom.txt")
"""