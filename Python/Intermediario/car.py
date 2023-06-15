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
# -> Limpa Terminal:
def clear_terminal():
    os.system('cls' if os.name != 'posix' else 'clear')
    
# ---- Project ---- #
while True:
    user = input('')
    