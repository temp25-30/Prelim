#python version 3.11.5

#part 1========================
txt = "Hello, World!"

print(txt[7:12])
print(txt.upper())

name = 'Python'
print(f"I love {name}")

print(10>9)
print(10==9)
print(10<9)

print(10>9)
print(10==9)
print(bool("Hello"))
print(bool(0))

a=15
b=4
print(a%b)
print(a//b)
print(a**b)
a+=10
b+=10
print(f"Value of a after:{a}")

thislist = ["apple", "banana", "cherry"]
print(thislist)
"""

#part 2==========================
"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"Maksuda Sultana")
print(thislist)

thislist.remove("Maksuda Sultana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#list traverse
thislist = ["apple", "banana", "cherry"]
thislist.append("Maksuda Sultana")
for i in range(len(thislist)):
    print(thislist[i])

print("\n")

rgb = ["red", "green", "blue"]
print(rgb[0])
rgb[1] = "yellow"
rgb.append("purple")
rgb.remove("red")

print(rgb)

thistuple=("apple","banana", "cherry")
print(thistuple)

thistuple="apple","banana", "cherry"
print(thistuple)
print(thistuple[-1])
print(thistuple[-2])
print(thistuple[-3])

thistuple=("apple","banana","cherry","orange","kiwi","melon", "mango")
print(thistuple[2:5])

#if else conditions
a=33
b=33
if b>a:
    print("b is greater than a")
elif b==a:
    print("b and a are equal")

a=200
b=33
if b>a:
    print("b is greater than a")
elif b==a:
    print("b and a are equal")
else:
    print("a is greater than b")

age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
