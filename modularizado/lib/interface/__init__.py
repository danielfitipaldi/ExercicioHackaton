def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def exibir_menu():
    cabecalho(f'Menu Principal')
    print(f'[ 1 ] Cadastrar Funcionário \n'
          '[ 2 ] Alterar tempo de empresa \n'
          '[ 3 ] Cadastrar valor da meta da empresa \n'
          '[ 4 ] Cadastrar faturamento da empresa \n'
          '[ 5 ] Exibir listagem de funcionários \n'
          f'[ 6 ] Sair \n')


def colorir(cor='padrao'):
    cores = {
        'padrao': '\033[m',  # 0 - sem cor
        'branco': '\033[1;30m',  # 1 - branco
        'vermelho': '\033[1;31m',  # 2 - vermelho
        'verde': '\033[1;32m',  # 3 - verde
        'amarelo': '\033[1;33m',  # 4 - amarelo
        'azul': '\033[1;34m',  # 5 - azul
        'roxo': '\033[1;35m',  # 6 - roxo
        'magenta': '\033[1;36m',  # 7 - magenta
        'cinza': '\033[1;37m'  # 8 - cinza
        }
    return cores[cor]


def msg_erro(msg):
    print(f'{colorir("vermelho")}{msg}{colorir("padrao")}')


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError) as err:
            print(f'Erro {err.__class__}. Por favor, digite um número inteiro válido')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError) as err:
            print(f'Erro {err.__class__}. Por favor, digite um valor numérico')
        except KeyboardInterrupt:
            print(f'Entrada de dados interrompida pelo usuário')
        else:
            return n

