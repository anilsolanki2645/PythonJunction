dict1 = {"anil":"solanki",
         "kuldip":"parmar",
         "amit":"rathod",
         "jay":"mahya"}

dict2 = {"anil":"rank1",
         "kuldip":"rank2",
         "amit":"rank3",
         "jay":"rank4"}

dict3 = {"anil":"32",
         "kuldip":"18",
         "amit":"25",
         "jay":"11"}

people = [ dict1, dict2, dict3 ]


for name, sir in dict1.items():
    print(name, sir, end="\n")

##for name in list1:
##    print(name)

##print(type(people))
##
##for name in people:
##        
##    print(name)
##    print()

print("\t\t Access value of element in dict\n")

print(dict1["anil"])

print(dict2.get("anil"))

print("\t\t Nested dictionary\n")

dict4 = {"anil":"solanki",
         "kuldip":"parmar",
         "amit":{"location":"amreli","study":"mca","status":"single"},
         "jay":"mahya"}

print(dict4)

print("\n\t\t Add element in dictionary\n")

dict4["keval"] = "patel"

dict4["hasmukh"] = "makwana"

print(dict4)

print("\n\t\t delete element in dictionary\n")

del dict4["hasmukh"]

print(dict4)

print("\n\t\t copy dictionary\n")

dict5 = dict1.copy()

print(dict5)

print("\n\t\t update dictionary\n")

dict5.update({"keval":"patel"})

print(dict5)

print("\n\t\t print dictionary keys and items \n")

print(dict5.keys())

print()

print(dict5.items())







    
