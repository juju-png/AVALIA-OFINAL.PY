
#variavel com a denominação media e outra varivel com a denominação  quatidade
media =0 
quantidade = 0
# repete uma ação 6 vezes
for i in range(6):
    #pedir para o usúario colocar o valor  para ser armazenado em na variável "num"
    num = float(input(f'Digite o {i+1}° número: '))
    # nesta parte o programa pegarar a media e somarar ao num
    if num > 0:
     media = media + num
     #Se o num for maior que 0 adicionar 1 na variável positivo
     quantidade = quantidade + 1

#Mostra a quantidade de valores positivos
print(f"{quantidade} valores positivos")
#Mostra a média da lista "numeros"
print(f"{media/quantidade :0.1f}")