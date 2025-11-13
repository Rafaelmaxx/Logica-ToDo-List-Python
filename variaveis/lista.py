# Declaração

minha_lista = [1, 2, 3, 4, 5, "Rafael", True, False]

print ("Minha lista de exemplo", minha_lista)


# Exibindo a lista 

print(minha_lista[2]) # exibe "3"


# Selecionar de um elemento ao outro (fatiar(slice))

print(minha_lista[1:7])

# Fatiar do inicio ate meu alvo:

print("Fatiando do inicio", minha_lista[:5]) # exibe lalala [1, 2, 3, 4, 5]

"""
Métodos lista
"""
minha_lista2 = [5, 4, 3, 2, 1, 'Maximiano', False, True]

minha_lista2[5] = "Freitas"
print("minha lista 2", minha_lista2)


# Método append() adiciona um elemento ao final da lista
minha_lista2.append(6)
print("Após append(6)", minha_lista2)


# Método index
indice = minha_lista2.index(False)
print("indice", indice)


# Método inert(): insere um elemento em um indice especifico

minha_lista2.insert(2, 10)
print("apos o insert", minha_lista2)


# Método pop

elemento = minha_lista2.pop(2)
print("removido", elemento, minha_lista2) #removido 10 [5, 4, 3, 2, 1, 'Freitas', False, True, 6]


# Método remove

minha_lista2.remove(False)
print("False removido", minha_lista2)


# Método sort

minha_lista3 = [5, 12, 3, 6, 7, 9, 10]
minha_lista3.sort()
print("Apos o sort: ", minha_lista3) # Apos o sort:  [3, 5, 6, 7, 9, 10, 12]