# Verificador e Gerador de senhas com Python 🔑🐍

Repositório criado para praticar meus conhecimentos em Python.  
Trata-se de um programa que verifica se a senha informada pelo usuário se enquadra nos critérios de uma senha forte, quais sejam:
    a) mínimo de 8 caracteres;  
    b) pelo menos uma letra maiúscula;  
    c) pelo menos um número;  
    d) pelo menos um caractere especial.  
Caso a senha não se enquadre nos requisitos acima, o usuário pode gerar uma senha forte aleatória.

## geradorsenhas.py:
No arquivo geradorsenhas.py é definida a função geradora de senhas aleatórias.
```python
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
```
Na presente função, inicialmente, são importadas as bibliotecas 'random' e 'string'.  
Após, entramos no escopo da função *geradorsenhas()*, onde, de início, são definidas as listas "letras", "numeros" e "pontuacao", as quais utilizam funções da biblioteca 'string' para definir listas que englobam as letras maiúsculas e minúsculas, os numerais e os caracteres especiais (de pontuação).  
Em seguida, a lista "senha" é criada como uma lista vazia, sendo adicionados 8 digítos, obtidos aleatoriamente dentre os elementos das listas "letras", "numeros" e "pontuacao", criadas anteriormente. São utilizados 6 caracteres dentre as letras, 1 numeral e 1 caractere especial, todos selecionados pela função *random.choice*.  
Depois de gerada a senha, é chamada a função *random.shuffle*, a qual embaralha, mistura, os items dentro da lista **senha**, de modo que a senha gerada não seguirá necessariamente a ordem *letra-letra-letra-letra-letra-letra-numero-pontuacao*.  
Já embaralhada a senha, é exibida a mensagem final ao usuário informando a nova senha forte gerada, formatada como uma string simples, para facilitar a leitura.

## verificadorsenhas.py:
### Parte inicial do código:
```python
from geradorsenhas import *
import string

maiusculas = list(string.ascii_uppercase)
numeros = list(string.digits)
pontuacao = list(string.punctuation)
tem_maiuscula = False
tem_numero = False
tem_pontuacao = False

senha_do_usuario = input("Insira sua senha: ")
```
Na parte inicial do código, é importado todo o conteúdo do arquivo *geradorsenhas*, bem como a biblioteca string.  
A seguir, são definidas as variáveis "maiusculas", "numeros" e "pontuação", as quais constituem listas que contém, respectivamente, letras maiúsculas, numerais e caracteres especiais. Além disso, são definidas variáveis booleanas setadas inicialmente como False, as quais servirão para verificar a presença de letra maiúscula, numeral e caractere especial na senha indicada pelo usuário.  
Finalmente, é solicitado ao usuário que insira a senha que deseja verificar.

### Bloco for:
```python
for digito in senha_do_usuario:
    if digito in maiusculas:
        tem_maiuscula = True
    if digito in numeros:
        tem_numero = True
    if digito in pontuacao:
        tem_pontuacao = True
```
No presente bloco, é feita uma iteração pelos digítos da senha informada pelo usuário, para fins de verificar a existência dos requisitos mínimos, quais sejam, uma letra maiúscula, um numeral e um caractere especial.  
Caso seja encontrado pelo menos um dos itens elencados acima, as variáveis booleanas são alteradas para True.  
Como cada verificação é independente, não é criado um bloco if-elif-else, mas sim três if diferentes.

### Senha fraca X senha forte:
```python
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
    if len(senha_do_usuario) < 8:
        print("São necessários pelo menos 8 caracteres.")
```
Aqui, são definidas as variáveis *senha_fraca* e *senha_forte*. A primeira corresponde ao não preenchimento de nenhum dos requisitos para uma boa senha; ao passo que a segunda é o oposto, ou seja, o preenchimento de todos os requisitos. Em oposição às senhas forte e fraca, a senha mediana seria aquela que não se enquadra em nenhuma das duas categorias, ou seja, pelo menos um requisito é atendido, mas não todos.  
Assim, é iniciado um bloco if que traz mensagens para o caso de senhas fortes e fracas e, ainda, no caso de senha mediana, informa quais critérios não foram atendidos. Mais uma vez, como os critérios são independentes, são feitas verificações if independentes.

### Gerar uma senha forte:
```python
if not senha_forte:
    print("""Deseja gerar uma nova senha?
    [1] - SIM
    [2] - NÃO
""")
    gerar_senha = int(input("> "))
    if gerar_senha == 1:
        geradorsenhas()
```
Nessa parte final do código, caso a senha do usuário não seja uma senha forte, será dada a opção de gerar uma nova senha, que atenda aos requisitos. Caso o usuário deseje gerar uma nova senha, deve selecionar o opção '1', o que chama a função *geradorsenhas()* criada no arquivo anteriormente explicado.
