import re
cpf = re.sub(r'[^0-9]','',input('Informe o CPF: '))
if cpf[0] * len(cpf) == cpf:
    print('cpf é invalido, dados sequenciais.')
    exit()

first_digit =  (sum([int(digit) * regressive for digit, regressive in zip(cpf[:9], range(10, 1, -1))]) * 10) % 11
second_digit = (sum([int(digit) * regressive for digit, regressive in zip(cpf[:10], range(11, 1, -1))]) * 10) % 11
if first_digit > 9:
    first_digit=0
elif second_digit > 9:
    first_digit =0
elif cpf[9:] == f'{first_digit}{second_digit}':
    print('CPF "{}{}{}.{}{}{}.{}{}{}-{}{}" validado.'.format(*cpf))
else:
    print('CPF "{}{}{}.{}{}{}.{}{}{}-{}{}" invalido.'.format(*cpf))
# result = []
# for digit, regressive in zip(cpf, range(10, 1, -1)):
#     print(f'{digit}*{regressive}= {int(digit) * regressive}')
#     result.append(int(digit) * regressive)
# print(result,'=',sum(result))