### File Handling ###
import os


txt_file = open("./my_file.txt", "w+")
#print(txt_file.read())
#txt_file.read() NO!!!

txt_file.write("Mi nombre es Brais\nMi appelido es Moure\n35 años\nY mi lenguaje preferido es Python")
#Muestra los 10 primeros carateres
"""print(txt_file.read(10))"""

#Leer línea a línea
"""
print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readline())
"""

#print(txt_file.readlines())

txt_file = open("./my_file.txt", "r+")

print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)
txt_file.write("\nAunque también me gusta Kotlin")
#for line in txt_file.readlines():
#    print(line)
print(txt_file.readline())

txt_file.close()

#os.remove("./my_file.txt")

import json

json_file = open("./my_file.json","w+")

json_test = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":"35",
    1:["Python", "Swift", "Kotlin"],   
    "Website":"marca.com"
}

#print(type(json_test))

#json_file.write(json_test)

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("./my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["Nombre"])