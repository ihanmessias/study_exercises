'''[Etapas do projeto]:
1. Criar Loop -> Capturar dados
2. Menu -> Apresentação
3. Condição -> User
4. Remoção -> Locação
5. Adição -> Devolução
'''

# ---- Import Libs ---- #
import os

# ---- Funcs ---- #
# -> Clear Terminal:
def clear_terminal():
    os.system('cls' if os.name != 'posix' else 'clear')
# -> Menu:
def view_menu():
    print(' | '.join([f'[{i}] - {op}' for i, op in enumerate(menu_op)]))
    user = input('~ ')
    return user
# -> View Cars:
def view_cars():
    for i, car in enumerate(cars.items()):
        print(f'[{i}] {car[0]} - R${car[1]} /dia')
    
# ---- Project ---- #
# -> Menu Options:
menu_op = ['Mostrar portifólio', 'Alugar um carro', 'Devolver um carro']
# -> Cars:
cars = {'Chevrolet Tracker':120, 'Chevrolet Onix':90,
            'Hyundai HB20':85,'Hyundai Tucson':120,
            'Fiat Uno':60,'Fiat Mobi':70,'Fiat Pulse':130}

while True:    
    clear_terminal()
    print('Bem vindo á locadora de carros!\nO que deseja fazer?\n')
    user = view_menu()
    print(user)
    break
