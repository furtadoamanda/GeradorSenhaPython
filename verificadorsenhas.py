from geradorsenhas import *
import string

maiusculas = list(string.ascii_uppercase)
numeros = list(string.digits)
pontuacao = list(string.punctuation)
tem_maiuscula = False
tem_numero = False
tem_pontuacao = False

senha_do_usuario = input("Insira sua senha: ")

for digito in senha_do_usuario:
    if digito in maiusculas:
        tem_maiuscula = True
    if digito in numeros:
        tem_numero = True
    if digito in pontuacao:
        tem_pontuacao = True


senha_fraca = (len(senha_do_usuario) < 8) and (not tem_maiuscula) and (not tem_numero) and (not tem_pontuacao)
senha_forte = (len(senha_do_usuario) >= 8) and tem_maiuscula and tem_numero and tem_pontuacao

if senha_forte:
    print("Sua senha é forte!")
elif senha_fraca:
    print("Sua senha é muito fraca! A senha ideal deve conter no mínimo 8 caracteres, pelo menos 1 letra maiúscula, pelo menos 1 número e pelo menos 1 caractere especial.")
else:
    print("Sua senha pode ser melhorada.")
    if not tem_maiuscula:
        print("Falta uma letra maiúscula.")
    if not tem_numero:
        print("Falta um número.")
    if not tem_pontuacao:
        print("Falta um caractere especial.")

if not senha_forte:
    print("""Deseja gerar uma nova senha?
    [1] - SIM
    [2] - NÃO
""")
    gerar_senha = int(input("> "))
    if gerar_senha == 1:
        geradorsenhas()