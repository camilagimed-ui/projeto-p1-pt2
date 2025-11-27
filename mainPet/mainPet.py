'--------------------------------------------------PROJETO DO PETSHOP------------------------------------------------'

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
    print('Bem vindo ao Pet e Cia!!!')
    print('Escolha uma das opções abaixo: ')
    print('1 - Cadastro')
    print('2 - login')
    print('0 - Sair')

    opcao = int(input('digite uma opcao: '))


    if opcao == 0:
        break

    elif opcao != 1 and opcao != 2 and opcao != 0:
        print('digite uma opcao valida!!')

    elif opcao == 1:
        print('efetue seu cadastro!')
        nome = input('nome: ')
        senha = input('senha: ')
        senha2 = input('confirme sua senha: ')
        tipo = input('digite se voce é administrador ou cliente: ').lower()
        idade = int(input('idade: '))
        nomePet = input('digite o nome do seu pet: ')

        while True:
            if tipo != 'administrador' and tipo != 'cliente':
                print('tipo invalido,digite o tipo novamente!!')
                tipo = input('digite se voce é administrador ou cliente: ').lower()

            elif senha != senha2:
                print('tem certeza que digitou as duas senhas iguais? Tente novamente')
                senha = input('senha: ')
                senha2 = input('confirme sua senha: ')

            elif idade < 0 or idade > 110:
                print('idade invalida!!Digite novamente!!')
                idade = int(input('idade: '))

            else:
                possuiNome = 0
                for n in usuario:
                    if nome == n[0]:
                        print('Esse nome ja exite!!!Tente outro nome!!!')
                        possuiNome = 1
                        nome = input('nome: ')

                if possuiNome == 0:
                    usuario.append([nome, senha, tipo, idade, nomePet])
                    print(f'Parabens {nome}, voce foi cadastrado com sucesso!!')
                    break

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
                    print('1 - realizar compra')
                    print('2 - atendimento ao pet')
                    print('3 - avaliação do produto ou atendimento')
                    print('4 - Lista de desejos')
                    print('0 - sair')
                    opcao = int(input('digite que opcao deseja realizar: '))

                    if opcao == 0:
                        break

                    elif opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                        print('opcao invalida digite novamente')
                        opcao = int(input('digite que opcao deseja realizar: '))
                    elif opcao == 1:
                        print('Realize sua compra agora mesmo!')
                        for i in range(len(produtos)):
                            print(f'produtos | {produtos[i][0]} | valor | ${produtos[i][1]} ')

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
                        for h in range(len(atendimentoP)):
                            print(f'atendimento: {atendimentoP[h][0]} |  Valor: R${atendimentoP[h][1]} ')
                        print('Qual atendimento deseja realizar?')
                        atendimento = input('digite o atendimento que deseja realizar: ').lower()

                        for h in range(len(atendimentoP)):
                            if atendimento.lower() == atendimentoP[h][0].lower():
                                print('Atendimento encontrado com sucesso!')
                                print('agora realize o agendamento do horario que você deseja!!')

                                for h in range(len(HorariosD)):
                                    print(f'horarios disponiveis {HorariosD[h]}')

                                horario = input('digite o horario que deseja marcar: ')
                                if horario not in HorariosD:
                                    print('horario invalido!!')
                                    horario = input('digite o horario que deseja marcar: ')
                                else:
                                    if horario == '10h':
                                        if contador1 < 3:
                                            contador1 += 1
                                            print('horario marcado com sucesso!')
                                            for a in range(len(atendimentoP)):
                                                if atendimento == atendimentoP[a][0]:
                                                    valort += atendimentoP[a][1]
                                                    print(f'o valor total do atendimento foi R${valort}')
                                        else:
                                            print('esse horario esta cheio!')
                                            break
                                    elif horario == '12h':
                                        if contador2 < 3:
                                            contador2 += 1
                                            print('horario marcado com sucesso!')
                                            for a in range(len(atendimentoP)):
                                                if atendimento == atendimentoP[a][0]:
                                                    valort += atendimentoP[a][1]
                                                    print(f'o valor total do atendimento foi R${valort}')
                                        else:
                                            print('esse horario esta cheio!')
                                            break
                                    elif horario == '16h':
                                        if contador3 < 3:
                                            contador3 += 1
                                            print('horario marcado com sucesso!')
                                            for a in range(len(atendimentoP)):
                                                if atendimento == atendimentoP[a][0]:
                                                    valort += atendimentoP[a][1]
                                                    print(f'o valor total do atendimento foi R${valort}')
                                        else:
                                            print('esse horario esta cheio!')
                                            break
                                    elif horario == '18h':
                                        if contador4 < 3:
                                            contador4 += 1
                                            print('horario marcado com sucesso!')
                                            for a in range(len(atendimentoP)):
                                                if atendimento == atendimentoP[a][0]:
                                                    valort += atendimentoP[a][1]
                                                    print(f'o valor total do atendimento foi R${valort}')
                                        else:
                                            print('esse horario esta cheio!')
                                            break

                                    pagamento = float(input('Insira quanto de dinheiro você vai dar: '))
                                    while pagamento < 0 or pagamento < valort:
                                        print('Valor inválido! Digite novamente!')
                                        pagamento = float(input('Insira quanto de dinheiro você vai dar: '))

                                    if pagamento >= valort:
                                        troco = pagamento - valort
                                        print(f'Compra concluída com sucesso! Seu troco é: R${troco}')
                                    break
                        else:
                            print('atendimento não encontrado')
                        break

                    elif opcao == 3:
                        print('deixe sua avaliação e no que seria possivel a gente melhorar!')
                        Av = input('deixe sua a avaliação aqui: ')
                        avaliacao.append(Av)
                        print(avaliacao)
                        print('avaliação enviada com sucesso!')

                    elif opcao == 4:
                       
                        print('bem vindo a sua lista de desejos do pet e cia!')
                        item = input('digite o nome do item que deseja adicionar a sua lista de desejos: ').lower()
                        for b in range(len(produtos)):
                            if item in produtos[b][0].lower():
                                print(f'o produto {item} foi encontrado!')
                                listaD.append(item)
                                print(f'essa é sua lista de desejo atualmente {listaD}')
                                break
                        else:
                            print(f'o produto {item} não existe em nossa loja!')
            if tipo == 'administrador':
                print('escolha a opçao que deseja realizar!!!')

                while tipo == 'administrador':
                      while True:
                        print("Escolha uma das seguintes opções para prosseguir:")
                        print("1-Gerenciamento de Serviços")
                        print("2-Gerenciameto de Produtos")
                        print("3-Estoque")
                        print("4-Adoções de Pets")
                        print("5-Sair")
                        opcao = input("Digite uma das opções para continuar: ")
                        if opcao == "5":
                            break

                        elif opcao == "1":
                            while True:
                                print("---------GERENCIADOR DE SERVIÇOS------------")
                                print("Bem Vindo ao Gerenciador de Serviços")
                                print("Escolha uma das seguintes opções para prosseguir:")
                                print("a-Cadastro Flash de Serviço")
                                print("b-Buscar Serviço")
                                print("c-Listar Serviços")
                                print("d-Atualizar Serviço")
                                print("e-Remover Serviço")
                                print("f-Nenhuma das opções acima")
                                opcao_atendimentoP = input("Escolha uma das seguintes opções para prosseguir:").lower()
                                if opcao_atendimentoP == "f":
                                    break

                                elif opcao_atendimentoP == "a":
                                    print("--------CADASTRAMENTO FLASH-------")
                                    print("---------NOVO SERVIÇO------------")
                                    quantidade = int(input("Digite a quantidade de serviços que você deseja cadastrar:"))
                                    for s in range(quantidade):
                                        print(f'Serviço {s+1} de {quantidade}')
                                        nomeatentimentoP = input("Digite o nome do novo serviço:  ").lower()
                                        descricaoatentimentoP = input("Digite uma descrição para o novo serviço cadastrado:").lower()
                                        preco = float(input("Digite o valor do novo serviço R$: "))
                                        while preco < 0:
                                            print("Digite um preço válido!Tente Novamente!")
                                            preco = float(input("Digite o valor do novo serviço R$: "))
                                        
                                        HorariosS = int(input("Digite o horário do novo serviço entre 10 da manhã e 18 da tarde:"))
                                        while HorariosS < 10 or HorariosS > 18:
                                            print("Horário inválido! Digite um horário maior que 0.")
                                            HorariosS = int(input("Digite o horário do novo serviço:"))
                                            print("Horário Válido")

                                        atendimentoP.append([nomeatentimentoP,descricaoatentimentoP,HorariosS, preco, quantidade])
                                        print(f"O novo serviço é {nomeatentimentoP}\n Descrição: {descricaoatentimentoP}\n Preço - R$:{preco}\n Horário: {HorariosS}\n Cadastrados com sucesso.")

                                elif opcao_atendimentoP =="b":
                                    print("---------BUSCAR SERVIÇOS------------")
                                    buscar = input('Digite o produto que deseja buscar:').lower()
                                    atentimentoPEncontrado = 0
                                    for s in atendimentoP:
                                        if buscar.lower() in s[0].lower():
                                            print('------SERVIÇO ENCONTRADO--------')
                                            print(f'Nome:{s[0]}')
                                            print(f'Preço R$:{s[1]}')
                                            atentimentoPEncontrado = 1
                                        if atentimentoPEncontrado == 0:
                                            print('Serviço não encontrado')

                                elif opcao_atendimentoP == "c":
                                    print("---------LISTA DE SERVIÇOS------------") 
                                    for s in atendimentoP: 
                                        print(f"Produto: {s[0]} | Preço: {s[1]}")

                                elif atendimentoP == "d":
                                    print("---------ATUALIZAR LISTA DE SERVIÇOS------------")
                                    for indice in range(len(atendimentoP)):
                                        print(f"Serviço {indice} - Serviços {atendimentoP[indice][0]}")

                                    indice = int(input("Digite o indice que você deseja atualizar: "))
                                    while indice < 0 or indice >= (len(atendimentoP)):
                                        print("Indice Inválido.Tente novamente!")
                                        indice = int(input("Digite o indice que você deseja atualizar: "))

                                    print(f"Servico Atual: {atendimentoP[indice][0]}")
                                    print(f"Preço Atual: {atendimentoP[indice][1]}")

                                    novo_nome = input("Digite o nome do novo serviço: ").lower()
                                    novo_HorariosS = int(input("Digite o novo horário do novo serviço entre 10 da manhã e 18 da tarde:"))
                                    while novo_HorariosS < 10 or novo_HorariosS > 18:
                                        print("Horário inválido! Digite um horário maior que 0.")
                                        novo_HorariosS = int(input("Digite o horário do novo serviço:"))
                                    print("Horário Válido")

                                    novo_preco = float(input("Digite o novo preço do serviço: "))
                                    while novo_preco < 0:
                                            print("Digite um preço válido!Tente Novamente!")
                                            novo_preco = float(input("Digite o valor do novo serviço R$: "))

                                    novaSublistaatendimentoP = [novo_nome, novo_HorariosS, novo_preco]
                                    atendimentoP[indice] = novaSublistaatendimentoP
                                    print("Serviço atualizado com sucesso!!")

                                elif opcao_atendimentoP == "e":
                                    print("---------REMOVER SERVIÇOS------------")
                                    for indice in range(len(atendimentoP)):
                                        print(f"Serviço {indice} - Serviços {atendimentoP[indice][0]}")

                                    indice = int(input("Digite o indice que você deseja remover: "))
                                    while indice < 0 or indice >= (len(atendimentoP)):
                                        print("Indice Inválido.Tente novamente!")
                                        indice = int(input("Digite o indice que você deseja remover: "))

                                        atendimentoP.remove(atendimentoP[indice])

                                else:
                                    print('Erro, escolha uma opção correta')

                        elif opcao == "2":
                            while True:
                                print("---------GERENCIADOR DE PRODUTOS------------")
                                print("Bem Vindo ao Gerenciador de Produtos")
                                print("Escolha uma das seguintes opções para prosseguir:")
                                print("a-Cadastro Flash de Produto")
                                print("b-Buscar Produto")
                                print("c-Listar Produto")
                                print("d-Atualizar Produto")
                                print("e-Remover Produto")
                                print("f-Nenhuma das opções acima")
                                opcao_produtos = input("Escolha uma das seguintes opções para prosseguir:").lower()
                                if opcao_produtos == "f":
                                    break

                                elif opcao_produtos == "a":
                                    print("--------CADASTRAMENTO FLASH-------")
                                    print("---------NOVO PRODUTO------------")
                                    quantidadep = int(input("Digite a quantidade de produtos que você deseja cadastrar:"))
                                    for p in range(quantidade):
                                        print(f'Produto {p+1} de {quantidade}')
                                        nomeProduto = input("Digite o nome do novo produto:  ").lower()
                                        descricaoProduto = input("Digite uma descrição para o novo produto cadastrado:").lower()
                                        preco = float(input("Digite o valor do novo produto R$: "))
                                        while preco < 0:
                                            print("Digite um preço válido!Tente Novamente!")
                                            preco = float(input("Digite o valor do novo produto R$: "))

                                        produtos.append([nomeProduto,descricaoProduto, preco, quantidadep])
                                        print(f"O novo Produto é {nomeProduto}\n Descrição: {descricaoProduto}\n Preço - R$  {preco}\n Cadastrados com sucesso.")

                                elif opcao_produtos =="b":
                                    print("---------BUSCAR PRODUTOS------------")
                                    buscar = input('Digite o produto que deseja buscar:').lower()
                                    produtoEncontrado = 0
                                    for p in produtos:
                                        if buscar.lower() in p[0].lower():
                                            print('------PRODUTO ENCONTRADO--------')
                                            print(f'Nome:{p[0]}')
                                            print(f'Preço R$:{p[1]}')
                                            produtoEncontrado = 1
                                    if produtoEncontrado == 0:
                                            print('Produto não encontrado')

                                elif opcao_produtos == "c":
                                    print("---------LISTA DE PRODUTOS------------")
                                    for p in produtos: 
                                        print(f"Serviço: {p[0]} | Preço: {p[1]}")

                                elif opcao_produtos == "d":
                                    print("---------ATUALIZAR LISTA DE PRODUTOS------------")
                                    for indice in range(len(produtos)):
                                        print(f"Produto {indice} - Produtos {produtos[indice][0]}")

                                        indice = int(input("Digite o indice do produto que você deseja atualizar: "))
                                        while indice < 0 or indice >= (len(produtos)):
                                            print("Indice Inválido.Tente novamente!")
                                            indice = int(input("Digite o indice do produto que você deseja atualizar: "))

                                    print(f"Produto Atual: {produtos[indice][0]}")
                                    print(f"Preço Atual: {produtos[indice][1]}")

                                    novo_nomeP = input("Digite o nome do novo produto: ").lower()
                                    novo_precoP = float(input("Digite o novo preço do produto: "))

                                    novaSublistaProdutos = [novo_nomeP, novo_precoP,]
                                    produtos[indice] = novaSublistaProdutos
                                    print("Produto atualizado com sucesso!!")

                                elif opcao_produtos =="e":
                                    print("---------REMOVER PRODUTOS------------")
                                    for indice in range(len(produtos)):
                                        print(f"Produto {indice} - Produtos {produtos[indice][0]}")

                                        indice = int(input("Digite o indice que você deseja remover: "))
                                        while indice < 0 or indice >= (len(produtos)):
                                            print("Indice Inválido.Tente novamente!")
                                            indice = int(input("Digite o indice que você deseja remover: "))

                                            produtos.remove(produtos[indice])

                                else:
                                    print('Erro, escolha uma opção correta')

                        elif opcao =="3":
                            while True:
                                print("------ESTOQUE------")
                                print("Bem Vindo ao Estoque Geral")
                                print("a-Ver Estoque de Serviço")
                                print("b-Ver Estoque de Produto")
                                print("c-Atualizar Estoque")
                                print("d-Remover do Estoque")
                                print("e-Sair")
                                opcao = input("Digite uma das opções para continuar: ")
                                if opcao == "e":
                                    break

                                elif opcao == "a":
                                    print("-----ESTOQUE DE SERVIÇOS--------")
                                    if len(atendimentoP) == 0:
                                        print("Não há serviço no estoque.")
                                    
                                    else:
                                        print("-----ESTOQUE DE SERVIÇOS--------")
                                        for s in atendimentoP:
                                            print(f"Serviço:{s[0]} | Preço:{s[1]} | Quantidade:{s[2]} ")

                                elif opcao == "b":
                                    print("-----ESTOQUE DE PRODUTOS--------")
                                    if len(produtos) == 0:
                                        print("Não há produtos no estoque.")
                                        
                                    else:
                                        print("-----ESTOQUE DE PRODUTOS--------")
                                        for p in produtos:
                                            print(f"Produto:{p[0]} | Preço: {p[1]} | Quantidade:{p[2]}")

                                elif opcao == "c":
                                    print("-----ATUALIZAR ESTOQUE--------")
                                    escolhaEstoque = input("Você quer atualizar 'a'(serviços) ou 'b'(produtos)? ").lower()

                                    if escolhaEstoque == "a":
                                        print("-----ATUALIZAR ESTOQUE DE SERVIÇOS--------")
                                        for indice in range(len(atendimentoP)):
                                            print(f"Serviço{indice} - Serviço{atendimentoP[indice][0]}  (atual: {atendimentoP[indice][3]})")
                                        indice = int(input("Digite o indice do serviço que você deseja atualizar: "))
                                        while indice < 0 or indice >= (len(atendimentoP)):
                                            print("Indice Inválido.Tente novamente!")
                                            indice = int(input("Digite o indice do serviço que você deseja atualizar: "))

                                        novaQuantidade = int(input("Digite a nova quantidade: "))
                                        atendimentoP[indice][4] = novaQuantidade
                                        print("Estoque atualizado com sucesso.")

                                    elif escolhaEstoque == "b":
                                        print("-----ATUALIZAR ESTOQUE DE PRODUTOS--------")
                                        for indice in range(len(produtos)):
                                            print(f"Produto{indice} - Produtos{produtos[indice][0]}  (atual: {produtos[indice][3]})")
                                            indice = int(input("Digite o indice do produto que você deseja atualizar: "))
                                        while indice < 0 or indice >= (len(produtos)):
                                            print("Indice Inválido.Tente novamente!")
                                            indice = int(input("Digite o indice do produto que você deseja atualizar: "))

                                        novaQuantidade = int(input("Digite a nova quantidade: "))
                                        produtos[indice][2] = novaQuantidade
                                        print("Estoque atualizado com sucesso.")

                                elif opcao == "d":
                                    escolhaEstoque = input("Você quer remover 'a'(serviços) ou 'b'(produtos)? ").lower()

                                    if escolhaEstoque =="a":
                                        print("-----REMOVER DE ESTOQUE DE SERVIÇOS--------")
                                        for indice in range(len(atendimentoP)):
                                            print(f"Serviço {indice} - Serviços {atendimentoP[indice][0]}")

                                        indice = int(input("Digite o indice do serviço que você deseja remover: "))
                                        while indice < 0 or indice >= (len(atendimentoP)):
                                            print("Indice Inválido.Tente novamente!")
                                            indice = int(input("Digite o indice do serviço que você deseja remover: "))

                                            atendimentoP.remove(atendimentoP[indice])

                                    if escolhaEstoque =="b":
                                        print("-----REMOVER DE ESTOQUE DE PRODUTOS--------")
                                        for indice in range(len(produtos)):
                                            print(f"Produto {indice} - Produtos {produtos[indice][0]}")

                                        indice = int(input("Digite o indice do produto que você deseja remover: "))
                                        while indice < 0 or indice >= (len(produtos)):
                                            print("Indice Inválido.Tente novamente!")
                                            indice = int(input("Digite o indice do produto que você deseja remover: "))

                                            produtos.remove(produtos[indice])

                                else:
                                    print('Erro, escolha uma opção correta')

                        elif opcao =="4":
                            while True:
                                print("------GERENCIAMENTO DE ADOÇÕES PET & CIA------")
                                print("Bem Vindo ao Adoções & Cia")
                                print("Adote um bichinho,alegre sua vida e mude a vida dele!")
                                print("a-Cadastrar Pets")
                                print("b-Listar Pets Disponiveis")
                                print("c-Atualizar Pets Disponiveís")
                                print("d-Remover Pets")
                                print("e-Sair")

                                opcao = input("Digite uma das opções para continuar: ")
                                if opcao == "e":
                                    break

                                elif opcao =="a":
                                    print("--------CADASTRAMENTO FLASH-------")
                                    print("--------PETS---------")
                                    quantidadePets = int(input("Digite a quantidade de pets que você deseja cadastrar:"))
                                    for d in range(quantidadePets):
                                        print(f'Pet {d+1} de {quantidadePets}')
                                        nomePet = input("Digite o nome do pet:  ").lower()
                                        especiePet = input("Digite a espécie de pet:")
                                        descricaoPet = input("Digite uma descrição do pet:").lower()
                                        idadePet = float(input("Digite a idade do pet: "))
                                        while idadePet < 0:
                                            print("Digite uma idade válida!Tente Novamente!")
                                            idadePet = float(input("Digite a idade do pet: "))
                                        
                                        animaisAdocoes.append([nomePet, especiePet, descricaoPet, idadePet])
                                        print(f"O nome do pet é {nomePet}\n Espécie do Pet: {especiePet}\n Descrição do Pet:{descricaoPet}\n Idade do Pet: {idadePet}\n Cadastrados com sucesso.")

                                elif opcao =="b":
                                    print("-----LISTAR DE PETS DISPONIVEIS--------")
                                    if len(animaisAdocoes) == 0:
                                        print("Nenhum animal está disponível para ser adotado!")
                                    
                                    else:
                                        for d in animaisAdocoes: 
                                            print(f"Nome: {d[0]} | Espécie: {d[1]} | Idade: {d[3]}")

                                elif opcao =="c":
                                    print("-----ATUALIZAR PETS--------")
                                    for indice in range(len(animaisAdocoes)):
                                        print(f"Animal {indice} - Animais {animaisAdocoes[indice][0]}")

                                    indice = int(input("Digite o indice que você deseja atualizar: "))
                                    while indice < 0 or indice >= (len(animaisAdocoes)):
                                        print("Indice Inválido.Tente novamente!")
                                        indice = int(input("Digite o indice que você deseja atualizar: "))

                                    print(f"Nome do Pet Atual: {animaisAdocoes[indice][0]}")
                                    print(f"Espécie do Pet Atual: {animaisAdocoes[indice][1]}")
                                    print(f"Idade Atual: {animaisAdocoes[indice][3]}")

                                    novo_nomePet = input("Digite o nome do pet: ").lower()
                                    nova_especiePet = input("Digite a espécie do Pet:")
                                    nova_idadePet = float(input("Digite a idade do pet: "))

                                    while nova_idadePet < 0:
                                        print("Digite uma idade válida!Tente Novamente!")
                                        nova_idadePet = float(input("Digite a idade do pet: "))

                                    novaSublistaAdocoesPets = [novo_nomePet,nova_especiePet, nova_idadePet]
                                    animaisAdocoes[indice] = novaSublistaAdocoesPets
                                    print("Lista de Pets Disponiveís atualizada com sucesso!!")

                                elif opcao =="d":
                                    print("---------REMOVER PETS------------")
                                    for indice in range(len(animaisAdocoes)):
                                        print(f"Animal {indice} - Animais {animaisAdocoes[indice][0]}")

                                    indice = int(input("Digite o indice do pet que você deseja remover: "))
                                    while indice < 0 or indice >= (len(animaisAdocoes)):
                                        print("Indice Inválido.Tente novamente!")
                                        indice = int(input("Digite o indice do produto que você deseja remover: "))

                                        animaisAdocoes.remove(animaisAdocoes[indice])

                                else:
                                    print('Erro, escolha uma opção correta')
                                    

