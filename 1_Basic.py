# basic Syntax
print("hello python....")

# Indentation

i=6
print(i)

for j in range(1,10): # : is indentation
    print(i)
    i=i+1

print("\n\n\n")

# comment

# this is single line comment

""" this is multiline comment """

''' this is also multiline comment
gfahdgjwhrjwhjrhwer
sjbdgjashgfhsg
vhefdhvshfv'''

# variable

# initilization of variable
name = "Anil" 
en_no = 32
marks = 89
print(type(marks))

# printing value of variable

print(name)
print(en_no)
print(marks)
print("\n")

# assign single value to multiple variable

a=b=c = 902

print("a....",a)
print("b....",b)
print("c....",c)
print("\n")


# asiign multiple value to multiple variable

x,y,z=45,56,85

print("x....",x)
print("y....",y)
print("z....",z)

# local variable

def add():
    p=12
    q=45
    r=p+q
    print("Add....  ",r)

add()

#print(r) # r is define in only fuction


# global variable

d = 45 # declare outside of function
e =154

def minu():
    d=40
    v = e-d  # use in function
    print("v is...",v)

minu()

print("v...",e-d)


















