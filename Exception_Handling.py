# Exception Handling

# Exceptions versus Syntax Errors

"""
# [1] Python code before removing the syntax error  
string = "Python Exceptions"  
  
for s in string:  
    if (s != o:  
        print( s ) #SyntaxError """

"""
# [2] Python code after removing the syntax error

string = "Python Exceptions"  
  
for s in string:  
    if (s != o):  
        print( s )  # NameError: name 'o' is not defined """


"""
# [3] Python code to catch an exception and handle it using try and except code blocks  
   
a = ["Python", "Exceptions", "try and except"]  
try:  
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
     for i in range( 4 ):  
        print( "The index and element from the array is", i, a[i] )  
#if an error occurs in the try block, then except block will be executed by the Python interpreter       
except:  
    print ("Index out of range") # Index out of range  """


"""
# [4] Python code to show how to raise an exception in Python  
num = [3, 4, 5, 7]  
if len(num) > 3:  
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" ) # rais exception  """


"""
# [5] Python program to show how to use assert keyword  
# defining a function  
def square_root( Number ):  
    assert ( Number < 0), "Give a positive integer"  
    return Number**(1/2)  
  
#Calling function and passing the values  
print( square_root( 36 ) )  
print( square_root( -36 ) )   """


"""
# [6] Python program to show how to use else clause with try and except clauses  
  
# Defining a function which returns reciprocal of a number  
def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )  """

"""
# [7] Python code to show the use of finally clause  
   
# Raising an exception in try block  
try:  
    div = 4 // 0    
    print( div )  
# this block will handle the exception raised  
except ZeroDivisionError:  
    print( "Atepting to divide by zero" )  
# this will always be executed no matter exception is raised or not  
finally:  
    print( 'This is code of finally clause' )  """

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")



