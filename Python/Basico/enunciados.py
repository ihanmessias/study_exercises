"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# user = input('Informe um número inteiro: ')

# try:
#     if int(user) % 2 == 0:
#         print('O valor informado é um número par')
#     else:
#         print('O valor informado é um número impar')
# except:
#     print('O valor informado não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# user =  input('Informe a hora: 0-23')

# try:
#     if int(user) >= 0 and int(user) <= 11:
#         print('Bom dia')
#     elif int(user) >= 12 and int(user) <= 17:
#         print('Boa tarde')
#     elif int(user) >= 18 and int(user) <= 23:
#         print('Boa noite')
#     else:
#         print('Valor fora do padrão permitido')
# except:
#     print('Valor informado invalido, informe um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# user = input('Informe seu primeiro nome: ')

# if len(user) <= 4:
#     print('Curto')
# elif len(user) == 5 or len(user) == 6:
#     print('Normal')
# else:
#     print('Muito grande')