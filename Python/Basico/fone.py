# ---- Metodo 1 ---- #
numbers = [61996487935, 61996487935]
formatted_numbers = []

for n in numbers:
    formatted_numbers.append(f'({n[0]}{n[1]}) {n[2]}{n[3]}{n[4]}{n[5]}{n[6]}-{n[7]}{n[8]}{n[9]}{n[10]}')

print(formatted_numbers)

# ---- Metodo 2 ---- #
numbers = [61996487935, 61996487935]
formatted_numbers = []

for n in numbers:
	formatted_numbers.append('({}{}) {}{}{}{}{}-{}{}{}{}'.format(*str(n)))
'''[Nota Sobre desempacotamento utilizando o .format]
O "*" é usado para desempacotar uma sequência em argumentos posicionais. Quando você usa "*str(n)" em ".format(*str(n))",
você está desempacotando a string "n" em argumentos individuais para o método ".format".
Isso significa que cada caractere da string "n" será passado como um argumento separado para o método ".format".
Por exemplo, se "n" for igual a "'12345'", então "*str(n)" será equivalente a passar "'1', '2', '3', '4', '5'" como argumentos
separados para o método ".format".'''

print(formatted_numbers)

# ---- Metodo 3 ---- #
numbers = '61996487935' #or int 61996487935
formatted_numbers = '({}{}) {}{}{}{}{}-{}{}{}{}'.format(*numbers)