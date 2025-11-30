import funçõescami

usuario = []
produtos = [['ração',150 , 70] ,['shampoo' , 30 , 70] , ['condicionador' , 30 , 70],['brinquedo' , 20 , 70] , ['coleira' , 20 ,70],['casinha',80, 70] , ['caminha' ,100, 70] , ['caixa de transporte' , 210 ,70] , ['escova' , 25 , 70] , ['kit de perfume' , 150 , 70]]

animaisAdocoes = []
listaD = []
HorariosD = ['10h', '12h',  '16h', '18h']
servicos = []
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

atendimentoP = [['banho', 70, 3], ['tosa', 40, 3], ['banho e tosa', 100, 3], ['consulta', 120, 3]]
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
            if i[0] == nome and i[1] == senha:
                logado = 1

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

                        funçõescami.lerprodutos(produtos)

                        while True:
                            qtd = int(input('Digite a quantidade de produtos que deseja comprar: '))
                            while qtd <= 0 or qtd > len(produtos):
                                print('Quantidade inválida de produto! Digite novamente!')
                                qtd = int(input('Digite a quantidade de produtos que deseja comprar: '))

                            valorT = 0
                            q = 0  
                            while q < qtd:
                                produtoC = input(f'Digite o nome do produto número {q + 1} que deseja comprar: ')
                                achouP = 0

                                for i in range(len(produtos)):
                                    if produtoC.lower() == produtos[i][0].lower():
                                        print(f'Produto {produtos[i][0]} | Valor: ${produtos[i][1]} cada')
                                        achouP = 1

                                        if produtos[i][2] == 0:
                                            print('Produto esgotado!')
                                            break

                                        qProduto = int(input('Digite a quantidade desse produto que deseja levar: '))

                                        while qProduto <= 0 :
                                            print('Quantidade inválida. Digite novamente.')
                                            qProduto = int(input('Digite a quantidade desse produto que deseja comprar: '))

                                        if qProduto > produtos[i][2]:
                                            print(f'Estoque insuficiente! Só há {produtos[i][2]} unidades disponíveis.')
                                        else:
                                            produtos[i][2] = produtos[i][2] - qProduto 
                                            valorT = valorT + produtos[i][1] * qProduto
                                            q = q + 1  
                                            print(f'Você comprou {qProduto} {produtos[i][0]}')
                                        break

                                if achouP == 0:
                                    print('Produto não encontrado! Digite novamente.')

                            print(f'o valor total da compra foi de {valorT}')
                            pagamento = float(input('Insira quanto de dinheiro você vai dar: '))
                            while pagamento < 0 or pagamento < valorT:
                                print('Valor inválido! Digite novamente!')
                                pagamento = float(input('Insira quanto de dinheiro você vai dar: '))

                            if pagamento > valorT:
                                troco = pagamento - valorT
                                print(f'Compra concluída com sucesso! Seu troco é: R${troco}')
                                break
                            else:
                                print('Pagamento realizado com sucesso!Obrigada por realizar sua compra no Pet e Cia!')
                                break

                    elif opcao == 2:
                        print('escolha seu atendimento:')
                        valort = 0

                        funçõescami.leratendimentos(atendimentoP)

                        print('Qual atendimento deseja realizar?')
                        atendimento = input('digite o atendimento que deseja realizar: ').lower()

                        for h in range(len(atendimentoP)):
                            if atendimento.lower() == atendimentoP[h][0].lower():

                                print('Atendimento encontrado com sucesso!')
                                print('agora realize o agendamento do horario que você deseja!!')

                                for x in range(len(HorariosD)):
                                    print(f'horarios disponiveis {HorariosD[x]}')

                                horario = input('digite o horario que deseja marcar: ')

                                while horario not in HorariosD:
                                    print('horario invalido!!')
                                    horario = input('digite o horario que deseja marcar: ')

                                if horario == '10h':
                                    if contador1 < 3:
                                        contador1 += 1
                                        funçõescami.horario(atendimentoP, valort, atendimento)
                                    else:
                                        print('esse horario esta cheio!')
                                    break

                                elif horario == '12h':
                                    if contador2 < 3:
                                        contador2 += 1
                                        funçõescami.horario(atendimentoP, valort, atendimento)
                                    else:
                                        print('esse horario esta cheio!')
                                    break

                                elif horario == '16h':
                                    if contador3 < 3:
                                        contador3 += 1
                                        funçõescami.horario(atendimentoP, valort, atendimento)
                                    else:
                                        print('esse horario esta cheio!')
                                    break

                                elif horario == '18h':
                                    if contador4 < 3:
                                        contador4 += 1
                                        funçõescami.horario(atendimentoP, valort, atendimento)
                                    else:
                                        print('esse horario esta cheio!')
                                    break

                        else:
                            print('atendimento não encontrado')

                        break


                    elif opcao == 3:
                        funçõescami.av (avaliacao)

                    elif opcao == 4:
                        funçõescami.desejo (produtos)