from exHackaton.lib.interface import *


def cadastrarFuncionario():
    funcionario = {}
    funcionario['Nome'] = str(input(f'Nome: ')).upper()
    funcionario['Idade'] = leiaInt(f'Idade: ')
    funcionario['Tempo'] = leiaInt(f'Tempo de Empresa (anos): ')
    funcionario['Salario'] = leiaFloat(f'Salário: R$ ')
    funcionario['Salário Final'] = 0

    return funcionario


def listarFuncionario(funcionarios):
    for cadaFunc in funcionarios:
        print(f'Nome: {cadaFunc["Nome"]} - Idade: {cadaFunc["Idade"]} - Tempo de Empresa: {cadaFunc["Tempo"]} - '
              f'Salário: R$ {cadaFunc["Salario"]} - Salário Final: R$ {cadaFunc["Salário Final"]}')


def alterarCadastro(funcionarios):

    while True:
        nome = str(input('Nome do funcionário: '))
        for cadaFunc in funcionarios:
            while cadaFunc['Nome'].lower() != nome.lower():
                msg_erro('Nome não encontrado!')
                nome = str(input('Nome do funcionário: '))
            if cadaFunc['Nome'].lower() == nome.lower():
                cadaFunc['Tempo'] = leiaInt(f'Você deseja alterar o tempo de empresa de {cadaFunc["Nome"]}. Qual '
                                              f'é o novo valor? ')
                print(f'Valor alterado com sucesso. O tempo de empresa de {cadaFunc["Nome"]} '
                      f'agora é {cadaFunc["Tempo"]} anos. ')
                break
        break


def calcularSalario(funcionarios, faturamento=0, meta=0):
    partLucro = (faturamento - meta) / len(funcionarios)
    if faturamento > meta:
        for cadaFunc in funcionarios:
            if cadaFunc['Tempo'] >= 10:
                cadaFunc['Salário Final'] = cadaFunc['Salario'] + (cadaFunc['Salario'] * 2/100) + partLucro
            else:
                cadaFunc['Salário Final'] = cadaFunc['Salario'] + partLucro
    else:
        for cadaFunc in funcionarios:
            cadaFunc['Salário Final'] = cadaFunc['Salario']






