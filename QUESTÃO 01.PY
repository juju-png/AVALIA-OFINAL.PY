#Calcular o imposto de renda
# Solicita ao usuário que digite o salário para o cálculo do imposto
salário = float(input("Digite o salário para cálculo do imposto: "))

# Atribui o valor do salário à variável 'base' para uso posterior no cálculo do imposto
base = salário

# Inicializa a variável 'imposto' com o valor zero
imposto = 0
# 
# Verifica se o valor da 'base' é maior que 3000
if base > 3000:
    # Calcula o imposto adicionando 35% do valor que excede 3000 à variável 'imposto'
    imposto = imposto + ((base - 3000) * 0.35)
    # Atualiza o valor da 'base' para 3000, já que essa faixa foi alcançada
    base = 3000

# Verifica se o valor da 'base' é maior que 1000 (agora após a possível atualização)
if base > 1000:
    # Calcula o imposto adicionando 20% do valor que excede 1000 à variável 'imposto'
    imposto = imposto + ((base - 1000) * 0.20)

# Exibe na tela o salário original e o imposto a pagar formatados com duas casas decimais
print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salário, imposto))
