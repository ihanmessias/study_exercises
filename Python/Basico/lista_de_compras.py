"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# -->> Import Libs <<-- #
import os
# -->> Variaveis <<-- #
list_ = []  # <--- Lista de compras
AUTO = 2
# -->> Função para limpar o terminal <<-- #
def clear_terminal():
    os.system('cls' if os.name != 'posix' else 'clear')
# ---- Função para adicionar valor a lista ---- #
def add_list():
    add = input('Valor: ')
    list_.append(add)
    clear_terminal()    
# ---- Função para exibir a lista ---- #
def view_list():
    clear_terminal()
    print('Itens da Lista:')
    for i, l in enumerate(list_):
        print(f'[{i}]-{l}')
# ---- Função para remover item da lista ---- #
def remove_list():
    clear_terminal()
    view_list()
    remove = input("Escolha o índice para apagar: ")
    if remove.isdigit():
        for i, l in enumerate(list_):
            if i != int(remove):
                continue
            
            else:
                list_.remove(list_[i])
                clear_terminal()
    else:
        print('Índice invalido.')
# -->> APP <<-- #
clear_terminal()
while True:
    if not list_:
        print('\033[31;1mNada para listar (Lista vazia). ❌\033[m')
        
    user = input('\nSelecione uma ação\n[i]nserir [a]pagar [l]istar [s]air: ').lower()
    
    if user == 'i':
        add_list()
    elif user == 'a':
        remove_list()
    elif user == 'l':
        view_list()
    elif user == 's':
        clear_terminal()
        print('Você saiu com sucesso!\nOs valores informados foram salvos em um arquivo chamado \033[32;1mlista.txt\033[m em seu diretorio')
        exit()
    else:
        clear_terminal()
        print('\033[31;1mValor informado não corresponde ao solicitado. Tente Novamente.\033[m')