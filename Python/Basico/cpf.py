# -->> *Import Libs* <<-- #
import re
# -->> *Input* <<-- #
cpf = re.sub(r'[^0-9]','',input('Informe o CPF: '))
# -->> *Options* <<-- #
if cpf[0] * len(cpf) == cpf:
    print('cpf é invalido, dados sequenciais.')    
else:
    first_digit =  (sum([int(digit) * regressive for digit, regressive in zip(cpf[:9], range(10, 1, -1))]) * 10) % 11
    second_digit = (sum([int(digit) * regressive for digit, regressive in zip(cpf[:10], range(11, 1, -1))]) * 10) % 11
    first_digit, second_digit = (0 if id > 9 else id for id in (first_digit, second_digit))

    if cpf[9:] == f'{first_digit}{second_digit}':
        print('CPF "{}{}{}.{}{}{}.{}{}{}-{}{}" validado.'.format(*cpf))
    else:
        print('CPF "{}{}{}.{}{}{}.{}{}{}-{}{}" invalido.'.format(*cpf))