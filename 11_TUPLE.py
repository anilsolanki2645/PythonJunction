# TUPLE is unmutable and allow duplication

#Create Tuple

print("\t\t\t\t CREATE TUPLE \n ")

mytuple = ("apple", "banana", "cherry", "apple", "cherry", 40, 66, "kiwi", "melon", "mango")

print(mytuple)

print("\n\t\t\t\t TUPLE LENGTH \n ")

print(len(mytuple))

print("\n\t\t\t\t ACCESS TUPLE \n ")

print(mytuple[2])
print()

print(mytuple[-1])
print()

print(mytuple[1:5])
print()

print(mytuple[-6:-2])
print()

print(mytuple[0::2])
print()

print(mytuple[:3])
print()

print(mytuple[2:])
print()


print("\n\t\t\t\t APDATE , ADD , REMOVE TUPLE USING LIST \n ")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print()

print("\n\t\t\t\t UNPACKING OF TUPLE \n ")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print()

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits1

print(green)
print(yellow)
print(red)
print()

print(mytuple.count("cherry"))

print()

print(mytuple.index(40))





