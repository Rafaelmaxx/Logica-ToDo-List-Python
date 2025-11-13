lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)

for elemento in tupla:
    print(elemento)

print("\n")

pessoa = {"nome": "joao", "sobrenome": "maximiano", "idade": "20"}
for i in pessoa.keys():
    print(i)

for valor in pessoa.values():
    print(valor)
print("\n")


for chave, valor in pessoa.items():
    print(f"{chave}: {valor} teste")


print("\n")


"""Parte 2"""
#range(): intervalo numerico

for numero in range(5,10):
    print(numero)