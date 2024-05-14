# Python String Methods:
print("\n")
print("\t\t\t\t-----------------")
print("\t\t\t\t STRING METHODS")
print("\t\t\t\t-----------------")
print("\n")

#capitalize():	Converts the first character to upper case

print("\t\t\t\t--- capitalize() ---")
print("\n")

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)
print("\n")

#casefold():    Converts string into lower case

print("\t\t\t\t--- casefold() ---")
print("\n")


txt1 = "Hello, And Welcome To My World!"

x1 = txt1.casefold()

print(x1)
print("\n")

#center():	Returns a centered string

print("\t\t\t\t--- center() ---")
print("\n")

txt2 = "banana"

x2 = txt2.center(50)

print(x2)
print("\n")

#count():	Returns the number of times a specified value occurs in a string

print("\t\t\t\t--- count() ---")
print("\n")

txt3 = "I love apples, apple are my favorite fruit"

x3 = txt3.count("apple")

print(x3)
print("\n")

#encode():	Returns an encoded version of the string

print("\t\t\t\t--- encode() ---")
print("\n")

txt4 = "My name is Ståle"

x4 = txt4.encode()

print(x4)
print("\n")

#endswith():	Returns true if the string ends with the specified value

print("\t\t\t\t--- endswith() ---")
print("\n")

txt5 = "Hello, welcome to my world."

x5 = txt5.endswith(".")

print(x5)
print("\n")

#expandtabs():	Sets the tab size of the string

print("\t\t\t\t--- expandtabs() ---")
print("\n")

txt6 = "H\te\tl\tl\to"

x6 =  txt6.expandtabs(5)

print(x6)
print("\n")

#find():	Searches the string for a specified value and returns the position of where it was found

print("\t\t\t\t--- find() ---")
print("\n")

txt7 = "Hello, welcome to my world."

x7 = txt7.find("welcome")

print(x7)
print("\n")

#format():	Formats specified values in a string

print("\t\t\t\t--- format() ---")
print("\n")

txt8 = "For only {price:.2f} dollars!"
print(txt8.format(price = 49))
print("\n")

#index():    Searches the string for a specified value and returns the position of where it was found

print("\t\t\t\t--- index() ---")
print("\n")

txt9 = "Hello, welcome to my world."

x9 = txt9.index("welcome")

print(x9)
print("\n")

#isalnum():	Returns True if all characters in the string are alphanumeric

print("\t\t\t\t--- isalnum() ---")
print("\n")

txt10 = "Company12"

x10 = txt10.isalnum()

print(x10)
print("\n")

#isalpha():	Returns True if all characters in the string are in the alphabet

print("\t\t\t\t--- isalpha() ---")
print("\n")

txt11 = "CompanyX"

x11 = txt11.isalpha()

print(x11)
print("\n")

#isdecimal():	Returns True if all characters in the string are decimals

print("\t\t\t\t--- isdecimal() ---")
print("\n")

txt12 = "\u0033" #unicode for 3

x12 = txt12.isdecimal()

print(x12)
print("\n")

#isdigit():	Returns True if all characters in the string are digits

print("\t\t\t\t--- isdigit() ---")
print("\n")

txt13 = "50800"

x13 = txt13.isdigit()

print(x13)
print("\n")

#isidentifier():    Returns True if the string is an identifier

print("\t\t\t\t--- isidentifier() ---")
print("\n")

txt14 = "Demo"

x14 = txt14.isidentifier()

print(x14)
print("\n")

#islower():	Returns True if all characters in the string are lower case

print("\t\t\t\t--- islower() ---")
print("\n")

txt15 = "hello world!"

x15 = txt15.islower()

print(x15)
print("\n")

#isnumeric():	Returns True if all characters in the string are numeric

print("\t\t\t\t--- isnumeric() ---")
print("\n")

txt16 = "454421"

x16 = txt16.isnumeric()

print(x16)
print("\n")

#isprintable():	Returns True if all characters in the string are printable

print("\t\t\t\t--- isprintable() ---")
print("\n")

txt17 = "Hello! Are you #1?"

x17 = txt17.isprintable()

print(x17)
print("\n")

#isspace():	Returns True if all characters in the string are whitespaces

print("\t\t\t\t--- isspace() ---")
print("\n")

txt18 = "   "

x18 = txt18.isspace()

print(x18)
print("\n")

#istitle():	Returns True if the string follows the rules of a title
#Check if each word start with an upper case letter:

print("\t\t\t\t--- istitle() ---")
print("\n")

txt19 = "Hello, And Welcome To My World!"

x19 = txt19.istitle()

print(x19)
print("\n")

#isupper():	Returns True if all characters in the string are upper case

print("\t\t\t\t--- isupper() ---")
print("\n")

txt20 = "THIS IS NOW!"

x20 = txt20.isupper()

print(x20)
print("\n")

#join():	Joins the elements of an iterable to the end of the string

print("\t\t\t\t--- join() ---")
print("\n")

myTuple = ("John", "Peter", "Vicky")

x21 = "#".join(myTuple)

print(x21)
print("\n")

#ljust():	Returns a left justified version of the string

print("\t\t\t\t--- ljust() ---")
print("\n")

txt22 = "banana"

x22 = txt22.ljust(20)

print(x22, "is my favorite fruit.")
print("\n")

#lower():	Converts a string into lower case

print("\t\t\t\t--- lower() ---")
print("\n")

txt23 = "Hello my FRIENDS"

x23 = txt23.lower()

print(x23)
print("\n")

#lstrip():	Returns a left trim version of the string

print("\t\t\t\t--- lstrip() ---")
print("\n")

txt24 = "     banana     "

x24 = txt24.lstrip()

print("of all fruits", x24, "is my favorite")
print("\n")

#maketrans():	Returns a translation table to be used in translations

print("\t\t\t\t--- maketrans() ---")
print("\n")

txt25 = "Hello Sam!"
mytable = txt25.maketrans("S", "P")
print(txt25.translate(mytable))
print("\n")

#partition():	Returns a tuple where the string is parted into three parts

print("\t\t\t\t--- partition() ---")
print("\n")

txt26 = "I could eat bananas all day"

x26 = txt26.partition("bananas")

print(x26)
print("\n")

#replace():	Returns a string where a specified value is replaced with a specified value

print("\t\t\t\t--- replace() ---")
print("\n")

txt27 = "I like bananas"

x27 = txt27.replace("bananas", "apples")

print(x27)
print("\n")

#rfind():	Searches the string for a specified value and returns the last position of where it was found

print("\t\t\t\t--- replace() ---")
print("\n")

txt28 = "Mi casa, su casa."

x28 = txt28.rfind("casa")

print(x28)
print("\n")

#rindex():	Searches the string for a specified value and returns the last position of where it was found

print("\t\t\t\t--- rindex() ---")
print("\n")

txt29 = "Mi casa, su casa."

x29 = txt29.rindex("casa")

print(x29)
print("\n")

#rjust():	Returns a right justified version of the string

print("\t\t\t\t--- rjust() ---")
print("\n")

txt30 = "banana"

x30 = txt30.rjust(20)

print(x30, "is my favorite fruit.")
print("\n")

#rpartition():	Returns a tuple where the string is parted into three parts

print("\t\t\t\t--- rjust() ---")
print("\n")

txt31 = "I could eat bananas all day, bananas are my favorite fruit"

x31 = txt31.rpartition("bananas")

print(x31)
print("\n")

#rsplit():	Splits the string at the specified separator, and returns a list

print("\t\t\t\t--- rsplit() ---")
print("\n")

txt32 = "apple, banana, cherry"

x32 = txt32.rsplit(", ")

print(x32)
print("\n")

#rstrip():	Returns a right trim version of the string

print("\t\t\t\t--- rstrip() ---")
print("\n")

txt33 = "     banana     "

x33 = txt33.rstrip()

print("of all fruits", x33, "is my favorite")
print("\n")

#split():	Splits the string at the specified separator, and returns a list

print("\t\t\t\t--- split() ---")
print("\n")

txt34 = "welcome to the jungle"

x34 = txt34.split()

print(x34)
print("\n")

#splitlines():	Splits the string at line breaks and returns a list

print("\t\t\t\t--- splitlines() ---")
print("\n")

txt35 = "Thank you for the music\nWelcome to the jungle"

x35 = txt35.splitlines()

print(x35)
print("\n")

#startswith():	Returns true if the string starts with the specified value

print("\t\t\t\t--- startswith() ---")
print("\n")

txt36 = "Hello, welcome to my world."

x36 = txt36.startswith("Hello")

print(x36)
print("\n")

#strip():	Returns a trimmed version of the string

print("\t\t\t\t--- strip() ---")
print("\n")

txt37 = "     banana     "

x37 = txt37.strip()

print("of all fruits", x37, "is my favorite")
print("\n")

#swapcase():	Swaps cases, lower case becomes upper case and vice versa

print("\t\t\t\t--- swapcase() ---")
print("\n")

txt38 = "Hello My Name Is PETER"

x38 = txt38.swapcase()

print(x38)
print("\n")

#title():Converts the first character of each word to upper case

print("\t\t\t\t--- title() ---")
print("\n")

txt39 = "Welcome to my world"

x39 = txt39.title()

print(x39)
print("\n")

#translate():	Returns a translated string

print("\t\t\t\t--- translate() ---")
print("\n")

mydict1 = {83:  80}
txt40 = "Hello Sam!"
print(txt40.translate(mydict1))
print("\n")

#upper():	Converts a string into upper case

print("\t\t\t\t--- upper() ---")
print("\n")

txt41 = "Hello my friends"

x41 = txt41.upper()

print(x41)
print("\n")

#zfill():	Fills the string with a specified number of 0 values at the beginning

print("\t\t\t\t--- zfill() ---")
print("\n")

txt42 = "50"

x42 = txt42.zfill(10)

print(x42)
