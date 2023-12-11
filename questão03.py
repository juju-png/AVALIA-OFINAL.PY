# Define uma função chamada verificar_senha que verifica se a senha digitada é igual à senha fixa
def verificar_senha(senha_digitada, senha_fixa):
    # Retorna True se a senha digitada for igual à senha fixa, caso contrário, retorna False
    return senha_digitada == senha_fixa

# Senha fixa (substitua pela sua senha real)
senha_fixa = "minhasenha123"

# Exemplo de uso
# Solicita ao usuário que digite a senha
senha_digitada = input("Digite a senha: ")

# Verifica se a senha digitada é igual à senha fixa usando a função verificar_senha
if verificar_senha(senha_digitada, senha_fixa):
    # Se a senha estiver correta, exibe uma mensagem de acesso permitido
    print("Senha correta! Acesso permitido.")
else:
    # Se a senha estiver incorreta, exibe uma mensagem de acesso negado
    print("Senha incorreta! Acesso negado.")
