'''
[Exercicío Cálculo IMC]:
- Data 30/05/2023
- Ihan Messias Nascimento dos Santos
- Python 3.10.6
'''
# ---- Import Libs ---- #
import os
import re

# Função para Limpeza de Terminal com base no SO
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')             

# Função para ciclo de continuidade
def continue_():
    user = input(f'{"="*60}'+'\nDeseja realizar um novo cálculo?\n[s/N]: ').upper()
    while True:
        if user == '' or user == 'N':
            clear_terminal()
            GODBYE = print('\033[1;32:41mObridado por útilizar a cálculadora de Índice de Massa Corporal (IMC). Volte sempre!🔚\033[m\n')
            exit()
        elif user == 'S':
            clear_terminal()
            break
        else:
            print('Valor informado não reconhecido, tente novamente.')           
# Loop
while True:
    # Saudação
    WELCOME = print('\033[1;32:41m🧮 Bem vindos a cálculadora de Índice de Massa Corporal (IMC):\033[m\n')
    
    # Captura de dados
    PESO = input('Me Informe seu peso: ')
    ALTURA = input('Me Informe sua altura utilizando somente números: ').replace(',','.')
    
    # Tratamento de dados
    PESO = re.sub(r'[^0-9.]', '', PESO)
    ALTURA = re.sub(r'[^0-9.]', '', ALTURA)
    ALTURA = float(ALTURA) / 100 if '.' not in ALTURA else float(ALTURA)
    
    # Função para Cálculo IMC
    IMC =  float(PESO)/(float(ALTURA) **2)
    
    # Condições:        
    if IMC < 18.4:
        CATEGORY = 'Magreza'
    elif IMC >= 18.5 and IMC <= 24.9:
        CATEGORY = 'Peso normal'
    elif IMC >= 25.0 and IMC <= 29.9:
        CATEGORY = 'Sobrepeso'
    elif IMC >= 30.0 and IMC <= 34.9:
        CATEGORY = 'Obesidade Grau I'
    elif IMC >= 35.0 and IMC <= 40.0:
        CATEGORY = 'Obesidade Grau II'
    elif IMC > 40.0:
        CATEGORY = 'Obesidade Grau III'
    
    # Retorno ao usuário
    print(f'\nPeso: {PESO}\nAltura: {ALTURA}\nSeu Índice de Massa Corporal é de: {IMC:.1f} e sua classificação é: "{CATEGORY}"')
    continue_()