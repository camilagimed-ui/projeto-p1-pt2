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

atendimentosP = [
    {'atendimento' : 'banho' , 'preco' : 70 , 'disponibilidade' : 3} ,
    {'atendimento' : 'tosa' , 'preco' : 40 , 'disponibilidade' : 3} ,
    {'atendimento' : 'banho e tosa' , 'preco' : 100 , 'disponibilidade' : 3} ,
    {'atendimento' : 'consulta' , 'preco' : 120 , 'disponibilidade' : 3}
] 

HorariosD = ['10h', '12h',  '16h', '18h']
avaliacao = []
valort = 0
usuario = [] 
listaD = []


def listaProdutos(produtos):
    for i in range(len(produtos)):
        print(f"produtos | {produtos[i]['nome']} | valor | ${produtos[i]['preco']}")


def listaratendimento(atendimentoP):
    for a in atendimentosP:
        print(f"atendimento: {a['atendimento']} | preço: ${a['preco']} | disponibilidade: {a['disponibilidade']}")


def av(avaliacao):
    print('deixe sua avaliação e no que seria possivel a gente melhorar!')
    av = input('deixe sua a avaliação aqui: ')
    avaliacao.append({
        'avaliacao' : av
    })
    print(avaliacao)
    print('avaliação enviada com sucesso!')


def desejo(produtos , listaD):
    print('bem vindo a sua lista de desejos do pet e cia!')
    item = input('digite o nome do item que deseja adicionar a sua lista de desejos: ').lower()
    
    for b in range(len(produtos)):
        if item == produtos[b]['nome'].lower():
            print(f'o produto {item} foi encontrado!')
            listaD.append({'desejo': item})

            for a in range(len(listaD)):
                print(f"essa é sua lista de desejo atualmente {listaD[a]['desejo']}")

            break

    else:
        print(f'o produto {item} não existe em nossa loja!')


def horario(atendimentoP , valort , atendimento):
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

            break



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
    senha = input('Senha: ')
    senha2 = input('Confirme sua senha: ')
    tipo = input('Digite se você é administrador ou cliente: ').lower()
    idade = int(input('Idade: '))
    nomePet = input('Nome do pet: ')

    if validarSenha(senha, senha2) == False:
        print('As senhas não são iguais!')
        return False

    elif validarIdade(idade) == False:
        print('Idade inválida!')
        return False

    elif nomeExiste(usuario, nome) == True:
        print('Esse nome já existe!')
        return False

    else:
        
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




listaratendimento(atendimentosP)
