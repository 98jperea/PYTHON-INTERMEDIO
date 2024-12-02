"""def sum_two_values(numero1,numero2):
    suma = numero1 + numero2
    print(suma)

sum_two_values(1,2)"""

sum_two_values = lambda numero1, numero2: numero1 * numero2

print(sum_two_values(5,5))

sum_two_values = lambda numero1, numero2: numero1 + numero2 -2 -1

print(sum_two_values(5,5))


#NO FUNCIONA
def sum_two_values(value):
    return lambda first,second,third: (first + second)*third +5

print(sum_two_values((1+2)*3))

