# Lista com a denominação "numeros"
numeros = []
# Variável com a denominação "impar"
impar = 0

# O loop irá repetir uma ação 5 vezes
for i in range(0, 5):
    # Pede para o usuário inserir os números
    numero = int(input(f'Digite o {i + 1}° número: '))
    # Adiciona o número à lista
    numeros.append(numero)
    # Se o número for ímpar, adiciona 1 à variável "impar"
    if numero % 2 != 0:
        impar = impar + 1

# Mostra quantos números ímpares existem na lista
print(f"{impar} valores ímpares na lista: {numeros}")
