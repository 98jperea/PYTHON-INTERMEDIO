import re

#my_string = "Esta es la lección de la lección número 7: Expresiones regulares"
my_string = "Esta es la lección de la Lección de la LEcción número 7: Expresiones regulares"

my_other_string = "Esta NO es la lección número 6: Manejo de ficheros"

"""print(re.match("Esta es la lección", my_string, re.I)) #No sé para qué sirve re.I
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares",my_string))"""

match = re.match("Esta es la lección", my_string, re.I)
print(match)
"""print(match.span()) #Imprime entre qué caracteres está"""
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta es la lección", my_other_string)
#if match != None:
#if not(match == None): #Lo mismo que fila 18
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares",my_string))

# Search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# Findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# Split

print(re.split("\n",my_string))
print(re.split(":", my_string))

# Sub

#print(re.sub("lección","LECCIÓN",my_string, re.I))
#print(re.sub("Expresiones regulares","RegEx", my_string))
#print(re.sub("lección|Lección","LECCIÓN", my_string))
#print(re.sub("lección|Lección", "LECCIÓN", my_string, re.I))
"""print(re.sub("lección|Lección", "LECCIÓN", my_string, re.I))
print(re.sub("LEcción", "LECCIÓN", my_string, re.I))"""
print(re.sub("[L|l]ección", "LECCIÓN", my_string, re.I))
#print(re.sub("[Le|le|LE]cción")) #ERROR

# Patterns

pattern = r"[lL]ección"
#print(re.findall(pattern,my_string))

pattern = r"[lL]ección|[Ee]xpresiones"
#print(re.findall(pattern,my_string))

pattern = r"[0-6]"
#print(re.findall(pattern,my_string))
#print(re.search(pattern,my_string))

pattern = r"[0-999]"
#print(re.findall(pattern,my_string))
#print(re.search(pattern,my_string))

"""pattern = r"\d" #Muestra números
print(re.findall(pattern,my_string))

pattern = r"\D" #Muestra todo menos números
print(re.findall(pattern,my_string))
"""
"""
pattern = r"L"
print(re.findall(pattern,my_string))

pattern = r"l"
print(re.findall(pattern,my_string))

pattern = r"L|l"
print(re.findall(pattern,my_string))

pattern = r"[L]"
print(re.findall(pattern,my_string))

pattern = r"[l]"
print(re.findall(pattern,my_string))

pattern = r"[L|l]"
print(re.findall(pattern,my_string))

pattern = r"[L|l]."
print(re.findall(pattern,my_string))

pattern = r"[L|l].*"
print(re.findall(pattern,my_string))
"""

#def is_valid_email(email):
email = "josepereabueno@hotmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))

email = "josepereabueno@hotmail.es.mx"
print(re.findall(pattern,email))

