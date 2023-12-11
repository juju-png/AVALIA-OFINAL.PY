
# Solicita ao usuário que digite seu número de telefone do Brasil
numero = int(input(f"Digite seu número de telefone do Brasil \n Obs: Não utilize espaços e nem sinais:"))

# Os dois primeiros dígitos do telefone serão salvos
# Transforma o número em string, pega os dois primeiros caracteres e converte de volta para int
numero = int(str(numero)[:2])

# Os dois números que foram salvos serão comparados e o programa identificará o seu DDD
if numero == 61:
    print("Brasília")
elif numero == 71:
    print("Salvador")
elif numero == 11:
    print("São Paulo")
elif numero == 21:
    print("Rio de Janeiro")
elif numero == 32:
    print("Juiz de Fora")
elif numero == 19:
    print("Campinas")
elif numero == 27:
    print("Vitória")
elif numero == 31:
    print("Belo Horizonte")
else:
    # Se o DDD não estiver registrado no sistema, exibe uma mensagem padrão
    print("Este DDD não está registrado no sistema")
