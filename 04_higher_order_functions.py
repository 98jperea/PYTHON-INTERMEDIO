def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values(first_value,second_value,f):
    return f(first_value + second_value)
#print(sum_two_values(5,2,sum_one))
#print(sum_two_values(5,2,sum_five))

#-------------------------------------------------------

#----Forma 1-----

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
"""print(add_closure(1))"""

#--------Forma 2--------

def sum_ten(value0):
    def add(value1):
        return value1 + 10 + value0
    return add

add_closure = sum_ten(1)

"""print(add_closure(1))"""

#---------Forma 3-------

#print(sum_ten(5)(1))

#----------------------------------

numbers = [2,5,10,21,3,30]

def multiply_two(number):
    return number * 2

#print(list(map(multiply_two,numbers)))

#Otra manera (con lambda, que es una función anónima)----

#print(list(map(lambda number: number * 2,numbers)))

# Filter

def filter_1(number):
    if number > 10:
        return True
    return False

#Con función

#print(list(filter(filter_1,numbers)))

#Con función lambda
#Filter es para filtrar, no para hacer operaciones combinando ambos parámetros (como ocurre con map)

#print(list(filter(lambda number: number > 10, numbers)))

#Reduce time

def sum_two_values(first_value, second_value):
    return first_value + second_value

from functools import reduce

#print(reduce(sum_two_values,numbers)) 

def sum_two_values(first_value, second_value):
    print(first_value)
    print(first_value)
    print(second_value)
    print(second_value)
    print("71")
    return first_value + second_value

print(reduce(sum_two_values,numbers))