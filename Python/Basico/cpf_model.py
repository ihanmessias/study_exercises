# -->> *Import Libs* <<-- #
import re
# -->>  *Input* <<-- #
'''
["re.sup"]: Remove qualquer caractere != 0 a 9 e substitui a ''.
'''
cpf = re.sub(r'[^0-9]','',input('Informe o CPF: '))
'''
["Dado sequencial"]: Realizar comparação com valor passado pelo cliente (usuário)  e faz checagem de dados sequenciais.
'''
if cpf[0] * len(cpf) == cpf:
    print('cpf é invalido, dados sequenciais.')    
    # exit()
else:
    '''
    [digit]: String com cpf tratado (Sem caracteres).
    [regressive]: range(10, 1, -1) --->> O que significa uma lista de contagem regressiva de 10 a 2 (Sendo que o segundo digito é re 11 a 2).
    [zip]: Pega o primeiro elemento do CPF e faz junção com primeiro elemento da contagem regressiva.
    [result and sum]: result é usado para armazenar todos os resultados númericos, depois é realizado a soma dos valores com "sum".
    [func]: Após soma é necessario a multiplicação por 10 e a divisão (restante) do resultado por 11. Por fim comparados com os digitos finais.

    EXEMPLO EXPLICATIVO:
        result = []
        for digit, regressive in zip(cpf, range(10, 1, -1)):
            print(f'{digit}*{regressive}= {int(digit) * regressive}') 
            result.append(int(digit) * regressive)
        print(result,'=',sum(result))
    '''
    first_digit =  (sum([int(digit) * regressive for digit, regressive in zip(cpf[:9], range(10, 1, -1))]) * 10) % 11
    second_digit = (sum([int(digit) * regressive for digit, regressive in zip(cpf[:10], range(11, 1, -1))]) * 10) % 11

    first_digit, second_digit = (0 if id > 9 else id for id in (first_digit, second_digit))
    # first_digit = 0 if first_digit > 9 else first_digit
    # second_digit = 0 if second_digit > 9 else second_digit

    if cpf[9:] == f'{first_digit}{second_digit}':
        print('CPF "{}{}{}.{}{}{}.{}{}{}-{}{}" validado.'.format(*cpf))
    else:
        print('CPF "{}{}{}.{}{}{}.{}{}{}-{}{}" invalido.'.format(*cpf))