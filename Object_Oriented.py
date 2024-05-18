print("***********Python Object Oriented Concept********\n")

#creating a class and methods
print("------------------creating a class and methods------------------\n")
class clg:
    def department(self):
        print("This is department of PGI")
        a = "MCA"
        b = "MBA"
        print("1.",a + "\n" + "2.", b + "\n")

    def mca_fac(self):
        print("Faculties of PGI MCA Department")
        a = "Priya Shah"
        b = "Momin Ayaz"
        print("1.",a + "\n" + "2.", b)
        

obj1 = clg()
obj1.department()
obj1.mca_fac()

#Creating class with constructor
print("------------------Creating class with constructor------------------\n")

class Student:
    def __init__(self,name,age,score,gender): #this init method is constructor

        self.name = name
        self.age = age
        self.score = score
        self.gender = gender

    def std_det(self):
        print("Name of Student is ",self.name)
        print("Age of Student is ",self.age)
        print("Score of Student is ",self.score)
        print("Gender of Student is ",self.gender)

##a = input("Enter Student Nmae....\n")
##b = int(input("Enter Student Age....\n"))
##c = int(input("Enter Student Score....\n"))
##d = input("Enter Student Gender....\n")

s = Student('Anil',23,95,'male')
#s = Student(a,b,c,d)
s.std_det()

###########################################################################################
#inheritance
print("*********************Inheritance*********************\n")

print("------------------(1)Single Inheritance------------------\n")

#Single inheritance
#create child class 
class Mba_student(Student):
    def mba_std_det(self):
        print("MBA student Detailes\n")

ms = Mba_student('Bhavik',21,100,'male')
ms.mba_std_det()
ms.std_det()

print("------------------(2)Multi-level Inheritance------------------\n")

#multi-level inheritance
#create child class 
class Toper_std(Mba_student):
    def mba_top_std_det(self):
        print("MBA Toper student Detailes\n")

ts = Toper_std('Kuldip',22,150,'male')
ts.mba_top_std_det()
ts.mba_std_det()
ts.std_det()

print("------------------(3)Multiple Inheritance------------------\n")

#multiple inheritance

#create first parent class 
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;
#create second parent class
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;
#create child class using first and second parent class
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;
#create object of child class and access method of all the class
d = Derived()  
print("Answer of First Parent class Calculation1....",d.Summation(10,20))  
print("Answer of Second Parent class Calculation2....",d.Multiplication(10,20))  
print("Answer of child class Derived....",d.Divide(10,20))


print("------------------(4)Hierarchical Inheritance------------------\n")

#Hierarchical inheritance

#create parent class 
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;
#create First Cild class using parent class
class Calculation2(Calculation1):  
    def Multiplication(self,a,b):  
        return a*b;
#create Second child class using parent class
class Derived(Calculation1):  
    def Divide(self,a,b):  
        return a/b;
#create object of First child class and access method of parent class
cl2 = Calculation2()
print("----------Calculation2 subclass access----------") 
print("Answer of Parent class Calculation1....",cl2.Summation(10,20))  
print("Answer of Second Parent class Calculation2....",cl2.Multiplication(10,20))  
#print("Answer of child class Derived....",d.Divide(10,20))

d = Derived()
print("----------Derived subclass access----------") 
print("Answer of Parent class Calculation1....",cl2.Summation(10,20))  
#print("Answer of Second Parent class Calculation2....",cl2.Multiplication(10,20))  
print("Answer of child class Derived....",d.Divide(10,20))

print("------------------(5)Hybrid Inheritance------------------\n")

#Hybrid inheritance

#create parent class 
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;
#create First Cild class using parent class
class Calculation2(Calculation1):  
    def Multiplication(self,a,b):  
        return a*b;
#create Second child class using parent class
class Derived(Calculation1):  
    def Divide(self,a,b):  
        return a/b;

#create last child class using Calculation2 and Derived
class Last(Calculation2,Derived):  
    def minus(self,a,b):  
        return a-b;
    
#create object of First child class and access method of parent class
cl2 = Calculation2()
print("\n----------Calculation2 subclass access----------") 
print("Answer of Parent class Calculation1....",cl2.Summation(10,20))  
print("Answer of Second Parent class Calculation2....",cl2.Multiplication(10,20))  
#print("Answer of child class Derived....",d.Divide(10,20))

d = Derived()
print("\n----------Derived subclass access----------") 
print("Answer of Parent class Calculation1....",cl2.Summation(10,20))  
#print("Answer of Second Parent class Calculation2....",cl2.Multiplication(10,20))  
print("Answer of child class Derived....",d.Divide(10,20))

ld = Last()
print("\n----------lats subclass access----------") 
print("Answer of Parent class Calculation1....",ld.Summation(10,20))  
print("Answer of Second Parent class Calculation2....",ld.Multiplication(10,20))  
print("Answer of child class Derived....",ld.Divide(10,20))
print("Answer of last child class Last....",ld.minus(100,20))

#############################################################################################

#polymorphism
print("*********************polymorphism*********************\n")

print("Description:\n Ability to work in a many forms \n or an entity can work in many formate")

print("1.Method Overloading\n2.Method Overriding\n3.Operator Overloading")

print("Important Note:\n    Method Overloading Can't Possible in Python But use With Conditional base")

print("------------------(1)Method Overloading------------------\n")

#Method Overloading

class overloading:
    def ovr_lod(self,x=None,y=None):
        if x==None and y==None:
            print("Hello this is python polymorphism")
            print("Enter value in method ovr_lod")
            print("Thanks for visit")

        elif x!=None and y==None:
            f=1
            for i in range(1,x+1):
                f=f*i
            print(f)

        else:
            print("addition of x and y is: ",(x+y))

ol=overloading()
ol.ovr_lod()
ol.ovr_lod(5)
ol.ovr_lod(45,48)

print("------------------(2)Method Overriding------------------\n")

#Method Overriding

class Bank:  
    def getroi(self):  
        return 10 
class SBI(Bank):  
    def getroi(self):
        return 7
  
class ICICI(Bank):  
    def getroi(self):  
        return 8 
b1 = Bank()  
b2 = SBI()  
b3 = ICICI()  
print("Bank Rate of interest:",b1.getroi()) 
print("SBI Rate of interest:",b2.getroi())
print("ICICI Rate of interest:",b3.getroi()) 

print("------------------(2.1)Super() Method------------------\n")

#Method Overriding

class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add
 
# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails
 
Emp_1 = Freelance(143, "Anil Solanki", "Ahmedabd" , "Anil@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

print("------------------(3)Operator Overloading------------------\n")

#Operator Overriding

class A:
    def __init__(self, a):
        self.a = a
  
    # adding two objects 
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
  
print(ob1 + ob2)
print(ob3 + ob4)

############################################################################################

print("*********************Encaptulation*********************\n")

#Encaptulation

"""This puts restrictions on accessing variables and methods directly
and can prevent the accidental modification of data.
"""

"""To prevent accidental change, an object’s \n variable can only be changed by
an object’s method. \n Those types of variables are known as private variables."""



"""Private members are similar to protected members,
the difference is that the class members declared private should neither be accessed
outside the class nor by any base class. In Python, there is no existence of Private
instance variables that cannot be accessed except inside a class.

However, to define a private member prefix the member name with double underscore “__”."""

print("\n ------------demonstrate private members------------ \n")

class Student:
   __privateVar = 27;
   def __display(self):
      print("I'm inside class myClass")
   def hello(self):
      print("Private Variable value: ",Student.__privateVar)
foo = Student()
foo.hello()
print(foo._Student__privateVar)
print(foo._Student__display())



############################################################################################

print("*********************Abstraction*********************\n")

#Abstraction

"""
Abstraction in python is defined as a process of handling complexity by
hiding unnecessary information from the user.

reduce complexity and increase the efficiency of the program.
"""
  
from abc import ABC  
class Car(ABC):
    pass
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  


