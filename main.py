estoque = []

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

# Cadastro de produtos
def cadastrar_produto(descricao, codigo, quantidade_estoque, custo_item, preco_venda):
    for produto in estoque:
        if produto['codigo'] == codigo:
            print(f"Produto com o código {codigo} já existe.")
            return
    
    novo_produto = {
        'descricao': descricao,
        'codigo': codigo,
        'quantidade_estoque': quantidade_estoque,
        'custo_item': custo_item,
        'preco_venda': preco_venda
    }

    estoque.append(novo_produto)
    print(f"Produto com o código {codigo} adicionado com sucesso!")
    return novo_produto

# Adicionar Estoque inicial
def adicionar_estoque_inicial():
    lista_estoque_inicial = estoque_inicial.split('#')
    
    for produto in lista_estoque_inicial:
        descricao, codigo, quantidade_estoque, custo_item, preco_venda = produto.split(';')
        
        codigo = int(codigo)
        quantidade_estoque = int(quantidade_estoque)
        custo_item = float(custo_item)
        preco_venda = float(preco_venda)
        
        cadastrar_produto(descricao, codigo, quantidade_estoque, custo_item, preco_venda)

adicionar_estoque_inicial()

# Listagem de produtos
def listar_produtos(lista_produtos = estoque):
    if not lista_produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print("Lista de Produtos:")
    print(f"{'Descrição':<30} {'Código':<10} {'Quantidade':<15} {'Custo':<10} {'Preço':<10}")
    print("-" * 75)
    
    for produto in lista_produtos:
        print(f"{produto['descricao']:<30} {produto['codigo']:<10} {produto['quantidade_estoque']:<15} {produto['custo_item']:<10} {produto['preco_venda']:<10}")

# Ordenação de produtos por quantidade
def ordenar_lista(tipo):
    if tipo.lower() == "crescente":
        estoque_ordenado = sorted(estoque, key=lambda x: x['quantidade_estoque'])
    elif tipo.lower() == "decrescente":
        estoque_ordenado = sorted(estoque, key=lambda x: x['quantidade_estoque'], reverse=True)
    else:
        return print("Digite 'crescente' ou 'decrescente'")
    return estoque_ordenado

lista_ordenada = ordenar_lista("decrsescente")
if lista_ordenada:
    listar_produtos(lista_ordenada)


