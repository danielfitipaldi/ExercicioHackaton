from exHackaton.lib.arquivo import *
from exHackaton.lib.interface import *

funcionarios = []
print(f'{colorir("azul")}OLÁ, SEJA BEM VINDO AO SISTEMA DA SUA EMPRESA{colorir("padrao")}')
while True:
    exibir_menu()
    opcao = leiaInt(f'{colorir("branco")}Escolha sua opção para prosseguir: {colorir("padrao")}')

    if opcao == 1:
        novo = cadastrarFuncionario()
        funcionarios.append(novo.copy())

    if opcao == 2:
        if len(funcionarios) == 0:
            msg_erro('Você ainda não cadastrou nenhum funcionário')
        else:
            alterarCadastro(funcionarios)

    if opcao == 3:
        metaEmpresa = leiaFloat('Meta da empresa: R$ ')

    if opcao == 4:
        faturamentoEmpresa = leiaFloat('Faturamento da empresa: R$ ')

    if opcao == 5:
        try:
            calcularSalario(funcionarios, faturamento=faturamentoEmpresa, meta=metaEmpresa or 0)
            listarFuncionario(funcionarios)
        except NameError:
            msg_erro('Você não definiu o faturamento e/ou a meta da empresa')
        except ZeroDivisionError:
            msg_erro('Você não cadastrou nenhum funcionário')

    if opcao == 6:
        break
print('-' * 30)
print('OBRIGADO E VOLTE SEMPRE!'.center(30))
print('-' * 30)
