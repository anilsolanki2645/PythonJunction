#LIST
print("\n")
print("\t\t\t\t\t--------")
print("\t\t\t\t\t  LIST  ")
print("\t\t\t\t\t--------")
print("\n")

#Create a LIST

print("\t\t\t\t---Create a LIST---")
print("\n")
lst = ["apple", "banana", "cherry"]
print(lst)
print("\n")

#Lists allow duplicate values

print("\t\t\t\t---Lists allow duplicate values---")
print("\n")
lst1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(lst1)
print("\n")

#List Length
print("\t\t\t\t---List Length---")
print("\n")
print(len(lst))
print("\n")

#List Items - Data Types

print("\t\t\t\t---List Items - Data Types---")
print("\n")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list4 = ["abc", 34, True, 40, "male"]

print(list4)
print("\n")

#Type

print("\t\t\t\t---Type---")
print("\n")

print(type(lst))
print("\n")

#list() Constructor

print("\t\t\t\t---list() Constructor---")
print("\n")

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print("\n")

#Access List Items

print("\n")
print("\t\t\t\t---------------------")
print("\t\t\t\t  Access List Items  ")
print("\t\t\t\t---------------------")
print("\n")

#Positive Indexing

print("\t\t\t\t---Positive Indexing---")
print("\n")

Alist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(Alist[2])
print("\n")

#Negative Indexing

print("\t\t\t\t---Negative Indexing---")
print("\n")

print(Alist[-1])
print("\n")

#Range of Indexes(Positive)

print("\t\t\t\t---Range of Indexes(positive)---")
print("\n")

print(Alist[2:5])
print("\n")

#Range of Indexes(Negative)

print("\t\t\t\t---Range of Indexes(Negative)---")
print("\n")

print(Alist[-5:-2])
print("\n")

#Starting

print("\t\t\t\t---Starting---")
print("\n")

print(Alist[:4])
print("\n")

#Ending

print("\t\t\t\t---Ending---")
print("\n")

print(Alist[4:])
print("\n")

#Check if Item Exists

print("\t\t\t\t---Check if Item Exists---")
print("\n")

if "kiwi" in Alist:
  print("Yes, 'apple' is in the fruits list")
print("\n")

#Change List Items

print("\n")
print("\t\t\t\t---------------------")
print("\t\t\t\t  Change List Items  ")
print("\t\t\t\t---------------------")
print("\n")

#Change Item Value

print("\t\t\t\t---Change Item Value---")
print("\n")

clist = ["apple", "banana", "cherry"]
clist[1] = "blackcurrant"
print(clist)
print("\n")

#Change a Range of Item Values

print("\t\t\t\t---Change a Range of Item Values---")
print("\n")

clist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
clist1[1:3] = ["blackcurrant", "watermelon"]
print(clist1)
print("\n")

#Insert Items

print("\t\t\t\t---Insert Items---")
print("\n")

clist2 = ["apple", "banana", "cherry"]
clist2.insert(2, "watermelon")
print(clist2)

#Add List Items

print("\n")
print("\t\t\t\t---------------------")
print("\t\t\t\t  Add List Items  ")
print("\t\t\t\t---------------------")
print("\n")

#Append Items

print("\t\t\t\t---Append Items---")
print("\n")

ailist = ["apple", "banana", "cherry"]
ailist.append("orange")
print(ailist)
print("\n")

#Insert Items

print("\t\t\t\t---Insert Items---")
print("\n")

ailist1 = ["apple", "banana", "cherry"]
ailist1.insert(1, "orange")
print(ailist1)
print("\n")

#Extend List

print("\t\t\t\t---Extend Items---")
print("\n")

Elist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
Elist.extend(tropical)
print(Elist)
print("\n")

#Add Any Iterable

print("\t\t\t\t---Add Any Iterable---")
print("\n")

Ilist = ["apple", "banana", "cherry"]
Ituple = ("kiwi", "orange")
Ilist.extend(Ituple)
print(Ilist)
print("\n")

#Remove List Items

print("\n")
print("\t\t\t\t---------------------")
print("\t\t\t\t  Remove List Items  ")
print("\t\t\t\t---------------------")
print("\n")

#Remove Specified Item

print("\t\t\t\t---Remove Specified Item---")
print("\n")

Rlist = ["apple", "banana", "cherry"]
Rlist.remove("banana")
print(Rlist)
print("\n")

#Remove Specified Index

print("\t\t\t\t---Remove Specified Index---")
print("\n")

Rlist1 = ["apple", "banana", "cherry"]
Rlist1.pop(1)
#Rlist.pop() - Remove last index by default
print(Rlist1)
print("\n")

#If you do not specify the index, the pop() method removes the last item.

#Clear the List

print("\t\t\t\t---Clear the List---")
print("\n")

Cllist = ["apple", "banana", "cherry"]
Cllist.clear()
print(Cllist)
print("\n")

#Delete the List

print("\t\t\t\t---Delete the List---")
print("\n")

Dlist = ["apple", "banana", "cherry"]
del Dlist[0]  #Delete specified index
print(Dlist)

del Dlist  #Delete list completly

#Loop Lists

print("\n")
print("\t\t\t\t---------------------")
print("\t\t\t\t  Loop List  ")
print("\t\t\t\t---------------------")
print("\n")

#Loop Through a List

print("\t\t\t\t---Loop Through a List---")
print("\n")

Llist = ["apple", "banana", "cherry"]
for x in Llist:
  print(x)
print("\n")

#Loop Through the Index Numbers

print("\t\t\t\t---Loop Through the Index Numbers---")
print("\n")

Llist1 = ["apple", "banana", "cherry"]
for i in range(len(Llist1)):
  print(Llist1[i])
  print(len(Llist1))
print("\n")

#Using a While Loop

print("\t\t\t\t---Using a While Loop---")
print("\n")

Wlist = ["apple", "banana", "cherry"]
i = 0
while i < len(Wlist):
  print(Wlist[i])
  i = i + 1
print("\n")

#Looping Using List Comprehension

print("\t\t\t\t---Looping Using List Comprehension---")
print("\n")

cmlist = ["apple", "banana", "cherry"]
[print(x) for x in cmlist]
print("\n")

#Condition Comprehension

print("\t\t\t\t---Condition Comprehension---")
print("\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
print("\n")

newlist1 = [x for x in range(10) if x < 5]
print(newlist1)
print("\n")

newlist2 = [x.upper() for x in fruits]
print(newlist2)
print("\n")

newlist3 = [x if x != "banana" else "orange" for x in fruits]
print(newlist3)
print("\n")

#Sort Lists

print("\n")
print("\t\t\t\t---------------------")
print("\t\t\t\t  Sort List  ")
print("\t\t\t\t---------------------")
print("\n")

#Sort List Alphanumerically

print("\t\t\t\t---Sort List Alphanumerically---")
print("\n")

ANlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
ANlist.sort()
print(ANlist)
print("\n")

ANlist1 = [100, 50, 65, 82, 23]
ANlist1.sort()
print(ANlist1)
print("\n")

#Sort Descending

print("\t\t\t\t---Sort Descending---")
print("\n")

SDlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
SDlist.sort(reverse = True)
print(SDlist)
print("\n")

SDlist1 = [100, 50, 65, 82, 23]
SDlist1.sort(reverse = True)
print(SDlist1)

#Customize Sort Function

print("\t\t\t\t---Customize Sort Function---")
print("\n")

def myfunc(n):
  return abs(n - 82)

Flist = [100, 50, 65, 82, 23]
Flist.sort(key = myfunc)
print(Flist)
print("\n")

#Case Insensitive Sort

print("\t\t\t\t---Case Insensitive Sort---")
print("\n")

CIlist = ["banana", "Orange", "Kiwi", "cherry"]
CIlist.sort()
print(CIlist)
print("\n")

CIlist.sort(key = str.lower)
print(CIlist)
print("\n")

#Reverse Order

print("\t\t\t\t---Reverse Order---")
print("\n")

CIlist1 = ["banana", "Orange", "Kiwi", "cherry"]
CIlist1.reverse()
print(CIlist1)
print("\n")

#Copy a List

print("\t\t\t\t---Copy a List---")
print("\n")

CIlist2 = ["banana", "Orange", "Kiwi", "cherry"]
colist = CIlist.copy()
print(colist)
print("\n")

colist1 = list(CIlist2)
print(colist)
print("\n")

#Join Two Lists

print("\t\t\t\t---Join Two List---")
print("\n")

list11 = ["a", "b", "c"]
list22 = [1, 2, 3]

list33 = list11 + list22
print(list33)
print("\n")

jlist = ["a", "b" , "c"]
jlist2 = [1, 2, 3]

for x in jlist2:
  jlist.append(x)

print(jlist)
print("\n")

jlist3 = ["a", "b" , "c"]
jlist4 = [1, 2, 3]

jlist3.extend(jlist4)
print(jlist3)






