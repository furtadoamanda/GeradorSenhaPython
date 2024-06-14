import random
import string

def geradorsenhas():
    letras = list(string.ascii_letters)
    numeros = list(string.digits)
    pontuacao = list(string.punctuation)

    senha = []
    digito_1 = senha.append(random.choice(letras))
    digito_2 = senha.append(random.choice(letras))
    digito_3 = senha.append(random.choice(letras))
    digito_4 = senha.append(random.choice(letras))
    digito_5 = senha.append(random.choice(letras))
    digito_6 = senha.append(random.choice(letras))
    digito_7 = senha.append(random.choice(numeros))
    digito_8 = senha.append(random.choice(pontuacao))

    random.shuffle(senha)

    print(f"*** Sua nova senha é: {senha[0]}{senha[1]}{senha[2]}{senha[3]}{senha[4]}{senha[5]}{senha[6]}{senha[7]}")

# Funciona, mas está muito feio
