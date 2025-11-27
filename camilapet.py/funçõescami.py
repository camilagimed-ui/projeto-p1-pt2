#criar funções para ler listas
#criar funções para pagamento
#criar funções para ler o menu
#criar funções apenas para aquilo que se repete mais de uma vez dentro do codigo e depois adaptar.
#!!!!perguntar a guilherme se é assim que faz!!!!!


produtos = [['ração',150 , 70] ,['shampoo' , 30 , 70] , ['condicionador' , 30 , 70],['brinquedo' , 20 , 70] , ['coleira' , 20 ,70],['casinha',80, 70] , ['caminha' ,100, 70] , ['caixa de transporte' , 210 ,70] , ['escova' , 25 , 70] , ['kit de perfume' , 150 , 70]]
HorariosD = ['10h', '12h',  '16h', '18h']
atendimentoP = [['banho', 70, 3], ['tosa', 40, 3], ['banho e tosa', 100, 3], ['consulta', 120, 3]]
avaliacao = []
valort = 0
usuario = [] 
listaD = []

def listaProdutos (produtos):
    for i in range(len(produtos)):
        print(f'produtos | {produtos[i][0]} | valor | ${produtos[i][1]} ')

def horarios (HorariosD):
    for h in range(len(atendimentoP)):
        print(f'atendimento: {atendimentoP[h][0]} |  Valor: R${atendimentoP[h][1]} ')

def av (avaliacao):
    print('deixe sua avaliação e no que seria possivel a gente melhorar!')
    Av = input('deixe sua a avaliação aqui: ')
    avaliacao.append(Av)
    print(avaliacao)
    print('avaliação enviada com sucesso!')

def desejo (produtos):
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


def horario (atentimentoP , valort , atendimento):
    print('horario marcado com sucesso!')
    for a in range(len(atendimentoP)):
        if atendimento == atendimentoP[a][0]:
            valort += atendimentoP[a][1]
            print(f'o valor total do atendimento foi R${valort}')
            pagamento = float(input('Insira quanto de dinheiro você vai dar: '))
            while pagamento < 0 or pagamento < valort:
                print('Valor inválido! Digite novamente!')
                pagamento = float(input('Insira quanto de dinheiro você vai dar: '))

            if pagamento >= valort:
                troco = pagamento - valort
                print(f'Compra concluída com sucesso! Seu troco é: R${troco}')
        break

def menuinicial ():
    print('Bem vindo ao Pet e Cia!!!')
    print('Escolha uma das opções abaixo: ')
    print('1 - Cadastro')
    print('2 - login')
    print('0 - Sair')


def menucompra():
    print('1 - realizar compra')
    print('2 - atendimento ao pet')
    print('3 - avaliação do produto ou atendimento')
    print('4 - Lista de desejos')
    print('0 - sair')