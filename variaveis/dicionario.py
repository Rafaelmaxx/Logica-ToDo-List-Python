# criando um dicionario
pessoa = {"nome": "Rafael", "idade": 30, "cidade": "Brasília"}

print(pessoa["nome"]) # Rafael
print(pessoa["idade"])


# adiciona valores no dicionario
pessoa["sobrenome"] = "Maximiano"
print(pessoa["sobrenome"]) #Maximiano



"""   Métodos   """


# atualizar dados

pessoa["idade"] = 12
print(pessoa["idade"]) # 12


# remover um par de chaves e valor
del pessoa["sobrenome"] # exclui a chave E o valor


# keys

chaves = pessoa.keys()
print(chaves) #dict_keys(['nome', 'idade', 'cidade'])


# para acessar os valores como se fosse uma lista:

chaves = list (pessoa.keys())
print("apos o list: ", chaves[0])
# apos o list:  nome


# values  -->  imprime apenas os valores do dicionario

valores = list(pessoa.values())
print("valor do indice 0 : ", valores[0]) 
# valor do indice 0 :  Rafael


"""
Items 

(ao inves de ter uma lista conm valores simples, 
cada elemento é uma tupla)
"""


items = list(pessoa.items())
print("Pares chave-valor do dicionario: ", items)
print("Primeiro valor: ", items[0])
# Primeiro valor:  ('nome', 'Rafael')