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
print('---------------- PRODUTOS ---------------- ')
for p in produtos:
    
    print(f'nome: {(p['nome'])} | preço: ${(p['preco'])} | estoque: {(p['estoque'])} unidades')
   
atendimentos = [
    {'atendimento' : 'banho' , 'preco' : 70 , 'disponibilidade' : 3} ,
    {'atendimento' : 'tosa' , 'preco' : 40 , 'disponibilidade' : 3} ,
    {'atendimento' : 'banho e tosa' , 'preco' : 100 , 'disponibilidade' : 3} ,
    {'atendimento' : 'consulta' , 'preco' : 120 , 'disponibilidade' : 3}
]

print('---------------- ATENDIMENTOS ---------------- ')
for a in atendimentos:
    
    print(f'atendimento: {(a['atendimento'])} | preço: ${(a['preco'])} | disponibilidade: {(a['disponibilidade'])} ')
