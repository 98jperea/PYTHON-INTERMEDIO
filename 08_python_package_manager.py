### Python Package Manager ###

# PIP https://pypi.org

#NUMPY
"""
import numpy

print(numpy.version.version)

numpy_array = numpy.array([1,2,3,4,5,6,7,8,9,10])
print(type(numpy_array))

print(numpy_array * 2)
"""

#PANDAS
import pandas

#REQUESTS
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
#print(response)
#print(response.status_code)
#print(response.json())

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1,4))

from myotherpackage import otherarithmetics
print(otherarithmetics.sum_two_values(1,2))

