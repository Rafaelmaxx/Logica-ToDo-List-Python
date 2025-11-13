# Declaração

nome_completo = "Rafael Maximiano"

nome_completo_aspas = """
Rafael maximiano
Apenas pular 
linhas
"""

nome_quebra = "Rafael \
Maximiano \
quebra de novo"

print (nome_completo, nome_completo_aspas, nome_quebra)

# Formatação

nome = 'rafael'
sobrenome = 'maximiano'

print ("1- Juntando com virgula:", nome_completo)
print ("2- Juntando com +: " + nome_completo)
print ("3- Juntando com outros +: " + nome_completo + " Gabriel " + "Pietra")
print ("4- Juntando com outros + e com ,: " + nome_completo, " Gabriel " + "Pietra")
print ("5- Juntando com outros + e com ,: " + nome_completo, " Gabriel " + "Pietra")
print ("6- Juntando com porcentagem S: %s" % nome_completo)
print ("7- Juntando com mais de uma porcentagem S: %s %s" %(nome, sobrenome))
print (f"8- Juntando com F: {nome} {sobrenome}")
print ("9- Juntando igual o F com format: {} {}".format(nome, sobrenome))

# Substituição de letras

nome2 = "Gabriela"


print (nome2.replace("a", "e"))