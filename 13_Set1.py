print("\t\t-----------------------------------")
print("\t\t\t\tSET")
print("\t\t-----------------------------------\n")

""" Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

Note:Sets are unordered, so you cannot be sure in which order the items will appear.
"""

#set prefer to add unique value

s1 = [1,2,3,4,5]

set1 = set(s1)

print(set1)

print(type(set1))

print("\t\tadd element in set\n")

set1.add(6)

print(set1)

print("\t\remove element in set\n")

set1.remove(5)

print(set1)




