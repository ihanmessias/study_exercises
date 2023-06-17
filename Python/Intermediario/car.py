# ---- Import Libs ---- #
import os

# ---- Funcs ---- #
def clear_terminal():
    """Clear Terminal"""
    os.system('cls' if os.name != 'posix' else 'clear')

def error_value():
    """Error Value"""
    clear_terminal()
    print('Erro no valor informado, escolha uma das opções com número correspondente.')

def continue_():
    """Continue"""
    while True:
        user = input('\nDeseja [0] Continuar ou [1] Sair?\n~ ')
        if user == '0':
            view_menu()
        elif user == '1':
            clear_terminal()
            print('Obrigado por utilizar nossa loja. Volte sempre!')
            exit()
        else:
            error_value()

def view_menu():
    """Menu"""
    clear_terminal()
    print('Bem vindo a locadora de carros!\nO que deseja fazer?\n')
    while True:
        print(' | '.join([f'[{i}] - {op}' for i, op in enumerate(menu_op)]))
        user = input('~ ')

        if user == '0':
            view_cars(cars=l_cars)
            continue_()
        elif user == '1':
            alug_cars()
            continue_()
        elif user == '2':
            devol_cars()
            continue_()
        else:
            error_value()         

def view_cars(cars):
    """View Cars"""
    clear_terminal()
    if l_cars:
        for i, car in enumerate(cars.items()):
            print(f'[{i}] {car[0]} - R${car[1]} /dia')
    else:
        print('Não há carros disponiveis.')
def alug_cars():
    """Alugando Cars"""
    clear_terminal()
    view_cars(l_cars)
    code_car = input('\nEscolha um dos carros disponiveis para alugar\n~ ')
    dias = input('Por quando dias?\n~ ')
    for i, car in enumerate(l_cars.items()):
        if code_car == str(i):
            print(f'\nVoce alugou o carro {car[0]} por {car[1] * int(dias)}')
            break
    alugados[car[0]] = l_cars.pop(car[0])

def devol_cars():
    """Devolução Cars"""
    clear_terminal()
    if alugados:
        view_cars(alugados)
        devol_car = input('\nEscolha um dos carros alugados para devolver\n~ ')
        for i, car in enumerate(alugados.items()):
            if devol_car == str(i):
                print(f'\nVoce devolveu o carro {car[0]}.')
                break
        l_cars[car[0]] = alugados.pop(car[0])    
    else:
        print("Não há carros alugados.")

# ---- Project ---- #
# -> Menu Options:
menu_op = ['Mostrar portifólio', 'Alugar um carro', 'Devolver um carro']
# -> Cars:
l_cars = {'Chevrolet Tracker':120, 'Chevrolet Onix':90,
          'Hyundai HB20':85,'Hyundai Tucson':120,
          'Fiat Uno':60,'Fiat Mobi':70,'Fiat Pulse':130}
alugados = {}

view_menu()