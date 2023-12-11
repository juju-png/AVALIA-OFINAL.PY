# Define uma função chamada calcular_aumento_salario que recebe dois parâmetros: salario_atual e percentual_aumento
def calcular_aumento_salario(salario_atual, percentual_aumento):
    # Calcula o valor do aumento aplicando o percentual sobre o salário atual
    aumento = salario_atual * (percentual_aumento / 100)
    
    # Calcula o novo salário somando o aumento ao salário atual
    novo_salario = salario_atual + aumento
    
    # Retorna o novo salário após o aumento
    return novo_salario

# Exemplo de uso da função
# Solicita ao usuário que digite o salário atual e o percentual de aumento
salario_atual = float(input("Digite o salário atual: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

# Chama a função calcular_aumento_salario com os valores fornecidos e armazena o resultado em novo_salario
novo_salario = calcular_aumento_salario(salario_atual, percentual_aumento)

# Exibe o novo salário após o aumento
print(f"O novo salário após o aumento é: {novo_salario}")
