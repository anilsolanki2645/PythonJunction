#The reduce(fun,seq) function is used to apply
#a particular function passed in its argument to all of the list
#elements mentioned in the sequence passed along.

#This function is defined in “functools” module.

from functools import reduce

num_list = [1,2,3,4,5]

sum1 = reduce(lambda x,y: x + y, num_list)

print(sum1,"\n\n") #15


def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [1, 2, 3, 4, 5]
total = reduce(sum, scores,2) # return a sum with +2
print(total)
