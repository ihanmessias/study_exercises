'''
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
'''
# ---- Import Libs ---- #
import os
import random
# Função para limpeza do terminal
def clear_terminal():
    os.system('cls' if os.name != 'posix' else 'clear')

# Palavra secreta
SECRET = random.choice(['casa','carro','cachorro','gato','amor','felicidade','alegria','paz','amizade','família'])
# Número de tentativas
count = 0
# Letras acertadas
win = set()

clear_terminal()
while True:
    user = input('Digite uma letra: ')
    # Validação de dado informado (Tratamento de erro)
    if user.isdigit() or len(user) != 1:
        clear_terminal()
        print('Digite somente uma letra')
        count += 1
        continue
    
    elif user in win:
        clear_terminal()
        print('Você já encontrou essa letra')
        count += 1
    elif user in SECRET and user not in win:
        clear_terminal()
        print(f'A letra "{user.upper()}" está presente na palavra secreta.')
        win.add(user.lower())
        count += 1
    else:
        clear_terminal()
        print(f'A letra {user} não se encontra na palavra secreta')
        count += 1
    
    secret = ''
    for i in SECRET:
        if i in win:
            secret += i
        else:
            secret += '*'
    print(f'Palavra secreta: {secret.capitalize()}\n')
    
    if len(secret) == len(SECRET) and '*' not in secret:
        clear_terminal()
        print(f'Acertou a palavra "{secret.capitalize()}"')
        print(f'Foram no total "{count} tentativas."')
        break