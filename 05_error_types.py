### Error Types ###

# SyntaxError
#print "¡Hola Comunidad!"
print("Hola Comunidad")

#NameError

language = "Spanish"
print(language)


#IndexError

my_list = ["Python","Fendi"]
print(my_list[0])
#print(my_list[2])


#ModuleNotFoundError

#import maths

import math

#AttributeError

#print(math.PI)

print(math.pi)


#KeyError

my_dict = {"Nombre":"Jose", "Apellido":"Perea"}
#print(my_dict["Edad"])
print(my_dict["Nombre"])


#TypeError

#print(my_list["Apellido"])
print(my_dict["Apellido"])
#print(my_list["0"])
print(my_list[0])

#ImportError

#from math import PI
#from math import PII

#from math import pi
def IMPORT_PI():
    from math import pi
    print(pi)

IMPORT_PI()

#ValueError

my_int = "10"
print(my_int)
print(type(my_int))

my_int = int("10")
print(my_int)
print(type(my_int))

"""my_int = int("10 años")
print(my_int)"""


#ZeroDivisionError

print(4/2,"Hola")
#print(4/0)
