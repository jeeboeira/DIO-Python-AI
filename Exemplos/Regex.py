import re

# Compile cria um padrão
string = "jesse"

pattern = re.compile("jesse")

#verifica se a string inteira atende
    #ao meu pattern definido
x = re.fullmatch(pattern, string)
print(x)

# re.search verifica  a primeira incidência
    #do padrão existe
string2 = "O jesse esta cansado hoje"
z = re.search(pattern, string2)
print(z)

# re.findall verifica todas as incidências
    #do padrão
string3 = "O jesse é o jesse né jesse"
findall = re.findall(pattern, string3)
print(findall)

# Sintaxe das regular expressions
# . representa qualquer caracter menos \n
pattern2 = re.compile(".....")
ponto = re.fullmatch(pattern2, string)
print(ponto)
# Para representar o caracter . uso \.

#^ representa o início da string
pattern3 = re.compile("^j....")
print(re.fullmatch(pattern3, string))

#% Representa o final da string

# [^] É diferente
pattern4 = re.compile("[^joao]")
print(re.findall(pattern4, string))

# \w is alfanum
# \W is not alfanum
# \s caracter vazio
# \S não vazio
# \d números de 0 a 9
# \D is not  0 a 9

#[] conjunto de possibilidades

# + Uma ou mais
# * zero ou mais
# ? zero ou uma

# {x} x vezes
# {y,z} mínimo e máximo de vezes