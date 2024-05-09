# Logical Operator

a,b,c = 70,52,45

# And Operator
def And():
    if a>b and b>c and c>a:
        print("true")
    else:
        print("false")
    print("\n")

And()

# OR Operator
def Or():
    if a>b or b>c or c>a:
        print("true")
    else:
        print("false")
    print("\n")

Or()

# Not Operator
def Not():
    if not(a<b):
        print("A is Greator than B")
    else:
        print("A is not Greator Than B")
    print("\n")

Not()
