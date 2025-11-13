# usando a função input


idade = int(input("quantos anos voce tem? ")) # int necessario para tansformar o valor em inteiro

if idade > 18:
    print("maior de idade")
elif idade == 18:
    print("Igual a 18")
else:
    print("Menor de idade")


# como fazer em uma linha só

mensagem = "pode tirar cnh" if idade >= 18 else "Nao pode tirar cnh"

print(mensagem)