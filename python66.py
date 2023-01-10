#ORDERED
#aLLOW DPLICATE
#uNCHANGEABLE  //Different from list //constant
#list is variable tuple is cosntant
#Dictonary is changable but doesnot allow duplication
#set do not contain duplicate ond unordered and unchangeable


#                          """TUPLE"""



"""
tup=("black","Blue","red",("yellow","orange","light green"),"white",225,"red")
print(tup)#print tuple
print(len(tup))#length of tuple
print(len(tup[3]))#length of tuple inside tuple
print(tup[3])
print(tup[3][2])#print the second item of third tuple

for i in tup:#print separately
    print(i)
print(tup.count("red"))#print number of red in tuple
"""
#Print single item in string an tupele type
"""
item=("ram")
print(type(item))

item1=("ram",)
print(type(item1))
"""
#concatination of tuple
"""
tup1=("black","Blue","red",("yellow","orange","light green"),"white",225,"red")
tup2=("orange","banana")
tup=tup1+tup2
print(tup)
"""

#print multiple time:
"""
tup1=("black","Blue","red",("yellow","orange","light green"),"white",225,"red")
print(tup1*3)

#assign value:
tu=(57, 25, 65,56,41)
(ram, shyam, hari, rosan, raj)=tu
print(ram)
print(tu[2])
print(max(tu))
print(min(tu))
"""



#                           """Dictionary"""
"""


dict={

    "brand" : "NewBalance",
    "type" : "Trouser",
    "color" : ("black","blue"),
    "Size" : "Medium, Large",
    "Available":7
}
dict2={
    "color":"white",

}
print(dict)

print(len(dict))
print(dict["brand"])#print the value at    brand key
dict["Size"]="x-large" #update the value in dict
print(dict)
for i in dict:
    print(i)
dict["types"]="simple" #add new data in the dictionary
print(dict)
print(type(dict))

"""

#                       """Set"""

"""

color={"red","blue","green"}
print(color)
print(type(color))
color.add("white")
print(color)
#color={"red","red"} //No duplication allowed
color.remove("red")
print(color)
color.pop()

print(color)
print(sorted(color))
print(color)
color.clear()

"""