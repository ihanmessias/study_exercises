# Definindo variáveis como funções
def soma_um(numero):
    return numero + 1

adiciona_um = soma_um
adiciona_um(5)


# Definindo funções dentro de outras funções
def soma_um(numero):
    def adiciona_um(numero):
        return numero + 1
    return adiciona_um(numero)
soma_um(4)


# Passando funções como argumentos de outras funções
def soma_um(numero):
    return numero + 1

def function_call(function):
    numero_to_add = 5
    return function(numero_to_add)

function_call(soma_um)


# Funções retornando outras funções
def funcao_ola():
    def diga_oi():
        return "Hi"
    return diga_oi
hello = funcao_ola()
hello()


# ---- Criando decoradores ---- #
def maiusculo(funcao):
    def retorno():
        func = funcao()
        return func.upper()
    return retorno

def diga_oi():
    return 'hello there'

funcao_decorada = maiusculo(diga_oi)
funcao_decorada()

# Com decorador
@maiusculo
def diga_oi():
    return 'hello there'

diga_oi()