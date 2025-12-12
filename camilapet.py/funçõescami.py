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
produtoC = ""
avaliacao = []
valort = 0
usuario = [] 
listaD = []

def menuinicial():
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

def listaProdutos(produtos):
    for i in range(len(produtos)):
        print(f"produtos | {produtos[i]['nome']} | valor | ${produtos[i]['preco']}")


def listaratendimento(atendimentoP):
    for a in range(len(atendimentoP)):
        print(f'atendimento | {atendimentoP[a]['atendimento']} | Valor | R$ {atendimentoP[a]['preco']}')


def acharAtendimento(atendimentoP , atendimento):
    
    for h in range(len(atendimentoP)):
        if atendimento.lower() == atendimentoP[h]['atendimento'].lower():
            print('Atendimento encontrado com sucesso!')
            print('agora realize o agendamento do horario que você deseja!!')
            return True
            break
            
    else:
        print('atendimento não encontrado! ')




def paghorario(atendimentoP , valort , atendimento):
    print('horario marcado com sucesso!')
    
    for a in range(len(atendimentoP)):
        if atendimento == atendimentoP[a]['atendimento']:
            valort += atendimentoP[a]['preco']
            print(f'o valor total do atendimento foi R${valort}')

            pagamento = float(input('Insira quanto de dinheiro você vai dar: '))

            while pagamento < 0 or pagamento < valort:
                print('Valor inválido! Digite novamente!')
                pagamento = float(input('Insira quanto de dinheiro você vai dar: '))

            if pagamento >= valort:
                troco = pagamento - valort
                print(f'Compra concluída com sucesso! Seu troco é: R${troco}')
                




    
def validarTipo(tipo):
    if tipo == 'administrador' or tipo == 'cliente':
        return True
    return False


def validarSenha(senha , senha2):
    if senha == senha2:
        return True
    return False


def validarIdade(idade):
    if idade > 0 and idade <= 110:  
        return True
    return False


def nomeExiste(usuario , nome):
    for n in usuario:
        if n['nome'] == nome:   
            return True
    return False


def cadastrarUsuario(usuario):
    print('Efetue seu cadastro!')

    nome = input('Nome: ')
    while nomeExiste(usuario, nome) == True:
        print('Esse nome já existe!')
        nome = input('Nome: ')

    senha = input('Senha: ')
    senha2 = input('Confirme sua senha: ')
    while validarSenha(senha, senha2) == False:
        print('As senhas não são iguais!')
        senha = input('Senha: ')
        senha2 = input('Confirme sua senha: ')
        
    tipo = input('Digite se você é administrador ou cliente: ').lower()
    while validarTipo(tipo) == False:
        print('tipo invalido')
        tipo = input('Digite se você é administrador ou cliente: ').lower()
        
    idade = int(input('Idade: '))
    while validarIdade(idade) == False:
        print('Idade inválida!')
        idade = int(input('Idade: '))

    nomePet = input('Nome do pet: ')

   

    
        
    usuario.append({
            'nome': nome,
            'senha': senha,
            'tipo': tipo,
            'idade': idade,
            'nome do pet': nomePet
        })

    with open('usuarios.txt', 'a') as arq:

            arq.write(f"Nome: {nome}\n")
            arq.write(f"Senha: {senha}\n")
            arq.write(f"Tipo: {tipo}\n")
            arq.write(f"Idade: {idade}\n")
            arq.write(f"Nome do Pet: {nomePet}\n")
            arq.write('-------------------------------------------------------\n')

    print(f'Parabéns {nome}, cadastro realizado com sucesso!')
    return True







def av(avaliacao):
    print('deixe sua avaliação e no que seria possivel a gente melhorar!')
    av = input('deixe sua a avaliação aqui: ')

    avaliacao.append({
        'avaliacao' : av
    })
    
    print(f'Avaliação: {av}')
    print('avaliação enviada com sucesso!')

    with open('avaliacao.txt', 'a') as arq:
        arq.write(f"avaliação: {av}\n")
        arq.write('-------------------------------------------------------\n')





def desejo(produtos , listaD):
    print('bem vindo a sua lista de desejos do pet e cia!')
    item = input('digite o nome do item que deseja adicionar a sua lista de desejos: ').lower()
    
    for b in range(len(produtos)):
        if item == produtos[b]['nome'].lower():
            print(f'o produto {item} foi encontrado!')
            listaD.append({'desejo': item})
            with open('lista_de_desejo.txt', 'a') as arq:
                arq.write(f"lista de desejo: {item}\n")

                arq.write('-------------------------------------------------------\n')

            for a in range(len(listaD)):
                print(f"essa é sua lista de desejo atualmente: {listaD[a]['desejo']}")


            break

    else:
        print(f'o produto {item} não existe em nossa loja!')

def pagamento(valorT):
        print(f'O valor total da compra foi de {valorT}')
        pagamento = float(input('Insira quanto de dinheiro você vai dar: '))
        while pagamento < 0 or pagamento < valorT:
            print('Valor inválido! Digite novamente!')
            pagamento = float(input('Insira quanto de dinheiro você vai dar: '))

        if pagamento > valorT:
            troco = pagamento - valorT
            print(f'Compra concluída com sucesso! Seu troco é: R${troco}')
            
        else:
            print('Pagamento realizado com sucesso! Obrigada por realizar sua compra no Pet e Cia!')
            
def compraraP(produtos):
    while True:
        qtd = int(input('Digite a quantidade de produtos que deseja comprar: '))
        while qtd <= 0 or qtd > len(produtos):
            print('Quantidade inválida de produto! Digite novamente!')
            qtd = int(input('Digite a quantidade de produtos que deseja comprar: '))
        valorT = 0
        q = 0  
        while q < qtd:
            achouP = 0
            produtoC = input(f'Digite o nome do produto número {q + 1} que deseja comprar: ')
            for i in range(len(produtos)):
                if produtoC.lower() == produtos[i]['nome'].lower():
                    achouP = 1
                    print(f"Produto {produtos[i]['nome']} | Valor: ${produtos[i]['preco']} cada")
                    if produtos[i]['estoque'] == 0:
                        print('Produto esgotado!')
                        break
                    qProduto = int(input('Digite a quantidade desse produto que deseja levar: '))
                    while qProduto <= 0:
                        print('Quantidade inválida. Digite novamente.')
                        qProduto = int(input('Digite a quantidade desse produto que deseja comprar: '))
                    if qProduto > produtos[i]['estoque']:
                        print(f"Estoque insuficiente! Só há {produtos[i]['estoque']} unidades disponíveis.")
                    else:
                        produtos[i]['estoque'] -= qProduto
                        valorT += produtos[i]['preco'] * qProduto
                        q += 1
                        print(f"Você comprou {qProduto} {produtos[i]['nome']}")
                    break
            if achouP == 0:
                print('Produto não encontrado! Digite novamente!')
                
        pagamento(valorT)
        break
