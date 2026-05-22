numeros = []

numero = int(input("Digite um número positivo (-1 para encerrar): "))
while numero != -1:
    numeros.append(numero)
    numero = int(input("Digite um número positivo (-1 para encerrar): "))

if numeros:
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)

    print(f"\nSoma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Menor número: {menor}")
    print(f"Maior número: {maior}")
else:
    print("Nenhum número foi inserido.")
