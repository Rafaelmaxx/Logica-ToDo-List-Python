# Condição falsa
False

# Condição verdadeira
True

if True:
    print("Será executado")

if False:
    print("não será executado")


# Operadores logicos and e or

if True and True:
    print("Será executado")

if True and False:
    print("não será executado, os dois valores precisam ser verdadeiros para executar a ação")

# OR

if True or True:
    print("Será executado")

if True or False:
    print("será executado, pois um dos dois precisa ser verdadeiro para executar")

if False or False:
    print("Não executa, pois nenhum valor é verdadeiro")