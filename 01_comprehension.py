my_original_list = [35,34,33,32,31,30]
#print(my_original_list)

#my_list = [i for i in my_original_list]
#my_list = [i for i in range(8)]
#print(my_list)

my_range = range(8)
#print(my_range)
#print(list(my_range))
#print(type(list(my_range)))
#print(type(my_range))

"""my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i + i for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)"""

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)