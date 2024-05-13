#Assign String to a Variable

print("**************")
print("String")
print("**************")

a = "Hello"
print(a)
print("\n")

#Multiline Strings

b = """Hello I Am Anil Solanki,
I Am a Student Of PGI,
My Frd Name Is Kuldip,
Jay,
Amit."""

print(b)
print("\n")

#Strings are Arrays

c = "Solanki"
print(c[5])
print(c[-2])
print("\n")

#Looping Through a String

d = "Anil Solanki"

for d in 'Solanki':
    print(d)
print("\n")

#String Length

e = "hello"
print(len(a))
print("\n")

#Check String

txt = "The best things in life are free!"
print("free" in txt)
print("\n")

if "free" in txt:
  print("Yes, 'free' is present.")
print("\n")

#Check if NOT

print("expensive" not in txt)
print("\n")

if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
print("\n")

#String Slicing
print("**************")
print("String Slicing")
print("**************")

g = "Hello, World!"
print(g[2:5])
print("\n")

#Slice From the Start

h = "Hello, World!"
print(h[:4])
print("\n")

#Slice To the End

print(h[4:])
print("\n")

#Negative Indexing

print(h[-5:-2])
print("\n")

#Modify Strings
print("**************")
print("Modify Strings")
print("**************")

print("\n")

#Upper Case

f = "anil solanki"
print(f.upper())
print("\n")

#Lower Case

i = "ANIL SOLANKI"
print(i.lower())
print("\n")

#Remove Whitespace

j = "Hello, World! "
print(j.strip())
print("\n")

#Replace String

print(j.replace("World", "Anil"))
print("\n")

#Split String

print(j.split("r"))
print("\n")

#String Concatenation

l = "Hello"
m = "World"
n = l + " " + m + " " + "Anil"
print(n)
print("\n")


#Formating a String

print("**************")
print("Formating Strings")
print("**************")

print("\n")

#we can not concate String to any other data type

ag = 22
tx = "My name is John, and I am {}"
print(tx.format(ag))
print("\n")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print("\n")

#with indexing
order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(order.format(quantity, itemno, price))


#Escape Characters
print("**************")
print("Escape Characters")
print("**************")

print("\n")

#Single Quote \'

txt1 = 'It\'s alright.'
print(txt1)
print("\n")

#Backslash   \\

txt2 = "This will insert one \\(backslash)."
print(txt2)
print("\n")

#New Line \n

txt3 = "Hello\nWorld!"
print(txt3)
print("\n")

#Carriage Return \r

txt4 = "Hello\r\rWorld!"
print(txt4) 
print("\n")

#Tab   \t

txt5 = "Hello\t\tWorld!"
print(txt5) 
print("\n")

#Backspace  \b

#This example erases one character (backspace):
txt6 = "Hello\bWorld!"
print(txt6)
print("\n")

#Form Feed   \f

txt7 = "Hello \f World!"
print(txt7)
print("\n")




