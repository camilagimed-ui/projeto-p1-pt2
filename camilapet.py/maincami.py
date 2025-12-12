import funçõescami

usuario = []
produtos = [
    {'nome': 'ração', 'preco': 150, 'estoque': 70},
    {'nome': 'shampoo', 'preco': 30, 'estoque': 70},
    {'nome': 'condicionador', 'preco': 30, 'estoque': 70},
    {'nome': 'brinquedo', 'preco': 20, 'estoque': 70},
    {'nome': 'coleira', 'preco': 20, 'estoque': 70},
    {'nome': 'casinha', 'preco': 80, 'estoque': 70},
    {'nome': 'caminha', 'preco': 100, 'estoque': 70},
    {'nome': 'caixa de transporte', 'preco': 210, 'estoque': 70},
    {'nome': 'escova', 'preco': 25, 'estoque': 70},
    {'nome': 'kit de perfume', 'preco': 150, 'estoque': 70}
]

atendimentoP = [
    {'atendimento' : 'banho' , 'preco' : 70 , 'disponibilidade' : 3} ,
    {'atendimento' : 'tosa' , 'preco' : 40 , 'disponibilidade' : 3} ,
    {'atendimento' : 'banho e tosa' , 'preco' : 100 , 'disponibilidade' : 3} ,
    {'atendimento' : 'consulta' , 'preco' : 120 , 'disponibilidade' : 3}
] 

HorariosD = [
    {'horario' : '10h'},
    {'horario' : '12h'},
    {'horario' : '16h'},
    {'horario' : '18h'},
]

animaisAdocoes = []
listaD = []
HorariosD = ['10h', '12h',  '16h', '18h']
servicos = []
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
avaliacao = []
valort = 0

while True:
    funçõescami.menuinicial()

    opcao = int(input('digite uma opcao: '))

    if opcao == 0:
        break

    elif opcao != 1 and opcao != 2 and opcao != 0:
        print('digite uma opcao valida!!')

    elif opcao == 1:
        funçõescami.cadastrarUsuario(usuario)

    if opcao == 2:
        print('faça o seu login!!')
        nome = input('digite seu nome: ')
        senha = input('digite sua senha: ')
        logado = 0

        for i in usuario:
            if i['nome'] == nome and i['senha'] == senha:
                logado = 1
                tipo = i['tipo']      

        if logado == 0:
            print('usuario nao encontrado!!!login invalido!!!')
        else:
            print(f'login efetuado com sucesso!!Bem vindo {nome}!!')

            if tipo == 'cliente':
                print('escolha a opçao que deseja realizar!!!')

                while tipo == 'cliente':
                    funçõescami.menucompra()

                    opcao = int(input('digite que opcao deseja realizar: '))

                    if opcao == 0:
                        break

                    elif opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                        print('opcao invalida digite novamente')
                        opcao = int(input('digite que opcao deseja realizar: '))
                        
                    elif opcao == 1:
                        print('Realize sua compra agora mesmo!')

                        funçõescami.listaProdutos(produtos)
                        
                        funçõescami.compraraP(produtos)

                    elif opcao == 2:
                        print('escolha seu atendimento:')
                        valort = 0

                        funçõescami.listaratendimento(atendimentoP)

                        print('Qual atendimento deseja realizar?')
                        atendimento = input('digite o atendimento que deseja realizar: ').lower()
                        funçõescami.acharAtendimento(atendimentoP , atendimento)

                        if funçõescami.acharAtendimento(atendimentoP , atendimento) == True:
                            for h in range(len(HorariosD)):
                                print(f'horarios: {HorariosD[h]['horario']}')

                            horario = input('digite o horario que deseja marcar: ')

                            while horario not in HorariosD:
                                print('horario invalido!!')
                                horario = input('digite o horario que deseja marcar: ')

                            if horario == '10h':
                                if contador1 < 3:
                                    contador1 += 1
                                    funçõescami.paghorario(atendimentoP, valort, atendimento)
                                    
                                else:
                                    print('esse horario esta cheio!')
                            elif horario == '12h':
                                if contador2 < 3:
                                    contador2 += 1
                                    funçõescami.pagorario(atendimentoP, valort, atendimento)
                                    
                                else:
                                    print('esse horario esta cheio!')
                            elif horario == '16h':
                                if contador3 < 3:
                                    contador3 += 1
                                    funçõescami.paghorario(atendimentoP, valort, atendimento)
                                    
                                else:
                                    print('esse horario esta cheio!')
                            elif horario == '18h':
                                if contador4 < 3:
                                    contador4 += 1
                                    funçõescami.paghorario(atendimentoP, valort, atendimento)
                                    
                                else:
                                    print('esse horario esta cheio!')
                           

                        

                    elif opcao == 3:
                        funçõescami.av(avaliacao)

                    elif opcao == 4:
                        funçõescami.desejo(produtos, listaD)
