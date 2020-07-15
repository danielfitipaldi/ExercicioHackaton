# Bem vindo
print('-' * 30)
print('BEM VINDO AO SISTEMA DA SUA EMPRESA'.center(30))
print('-' * 30)

# Menu
funcionario = {}
quadroDeFucionarios = []
faturamentoEmpresa = metaEmpresa = partLucro = opcao = 0

while True:
    try:
        opcao = int(input('[ 1 ] Cadastrar Funcionário \n'
                          '[ 2 ] Alterar tempo de empresa \n'
                          '[ 3 ] Cadastrar valor da meta da empresa \n'
                          '[ 4 ] Cadastrar faturamento da empresa \n'
                          '[ 5 ] Exibir listagem de funcionários \n'
                          '[ 6 ] Sair \n'
                          'Escolha sua opção para prosseguir: '))
    except (ValueError, TypeError, ZeroDivisionError):
        print('Opção inválida.')
    if opcao not in range(1, 7):
        try:
            opcao = int(input('Escolha uma das opções válidas para prosseguir: '))
        except (ValueError, TypeError, ZeroDivisionError):
            print('Opção inválida. ')

    if opcao == 1:
        funcionario.clear()
        print('-' * 30)
        print('CADASTRAR FUNCIONÁRIO'.center(30))
        print('-' * 30)
        funcionario['Nome'] = str(input('Nome: '))
        funcionario['Idade'] = int(input('Idade: '))
        funcionario['Tempo de empresa'] = int(input('Tempo de empresa (anos): '))
        funcionario['Salario Mensal'] = float(input('Salário: '))
        quadroDeFucionarios.append(funcionario.copy())

    if opcao == 2:
        print('-' * 30)
        print('ALTERAR TEMPO DE EMPRESA'.center(30))
        print('-' * 30)
        nomeAlterado = str(input('Digite o nome do funcionário: '))
        for c in range(len(quadroDeFucionarios)):
            if quadroDeFucionarios[c]['Nome'].lower() == nomeAlterado.lower():
                quadroDeFucionarios[c]['Tempo de empresa'] = int(input(f'Você deseja alterar o tempo de empresa '
                                                                       f'de {quadroDeFucionarios[c]["Nome"]}. '
                                                                                    f'Qual o novo valor? '))

    if opcao == 3:
        print('-' * 30)
        print('CADASTRAR VALOR DA META DA EMPRESA')
        metaEmpresa = float(input('Meta da empresa em R$: '))
        print('-' * 30)
    if opcao == 4:
        print('-' * 30)
        print('CADASTRAR FATURAMENTO DA EMPRESA')
        faturamentoEmpresa = float(input('Faturamento da empresa em R$: '))
        print('-' * 30)
    if opcao == 5:
        print('-' * 30)
        print('EXIBIR LISTAGEM DE FUNCIONÁRIOS')
        # Participação no Lucro = (faturamento - meta da empresa) / total de funcionários
        partLucro = (faturamentoEmpresa - metaEmpresa) / len(quadroDeFucionarios)
        if faturamentoEmpresa > metaEmpresa:
            for c in range(len(quadroDeFucionarios)):
                if quadroDeFucionarios[c]['Tempo de empresa'] >= 10:
                    quadroDeFucionarios[c]['Salário Final'] = quadroDeFucionarios[c]['Salario Mensal'] + \
                                                              (quadroDeFucionarios[c]['Salario Mensal'] * 2 / 100) \
                                                              + partLucro
                else:
                    quadroDeFucionarios[c]['Salário Final'] = quadroDeFucionarios[c]['Salario Mensal'] + partLucro
        else:
            for c in range(len(quadroDeFucionarios)):
                quadroDeFucionarios[c]['Salário Final'] = quadroDeFucionarios[c]['Salario Mensal']

        for cadaFunc in quadroDeFucionarios:
            print(f'Nome: {cadaFunc["Nome"]} Idade: {cadaFunc["Idade"]} Tempo de Empresa: {cadaFunc["Tempo de empresa"]} '
                  f'ano(s) Salário Mensal: {cadaFunc["Salario Mensal"]} Salário Final: {cadaFunc["Salário Final"]}')

        print('-' * 30)
    if opcao == 6:
        break
print('-' * 30)
print('OBRIGADO E VOLTE SEMPRE!'.center(30))
print('-' * 30)



