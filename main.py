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

# Busca de Produtos
def buscar_produtos(descricao='', codigo=''):
    produtos_encontrados = [] 
    for produto in estoque:
        if descricao:
            if descricao.lower() in produto['descricao'].lower():
                produtos_encontrados.append(produto)
        elif codigo:
            if produto['codigo'] == int(codigo):
                produtos_encontrados.append(produto)

    if produtos_encontrados:
        listar_produtos(produtos_encontrados)
    else:
        print("Produto não encontrado.")

# Remoção de produtos
def remover_produto(codigo):
    for produto in estoque:
        if produto['codigo'] == codigo:
            estoque.remove(produto)
            print(f"Produto com código {codigo} removido.")
            return
    print(f"Produto com código {codigo} não encontrado.")

# Consulta de produtos esgotados:
def listar_produtos_esgotados():
    produtos_esgotados = [] 
    for produto in estoque:
        if produto['quantidade_estoque'] == 0:
            produtos_esgotados.append(produto)

    if produtos_esgotados:
        listar_produtos(produtos_esgotados)
    else:
        print("Não há produtos esgotados.")

# Menu interativo
def menu():
    while True:
        print("\n===== MENU ======")
        print("1. Adicionar novo produto")
        print("2. Listar produtos cadastrados")
        print("3. Ordenar produtos pela quantidade")
        print("4. Buscar produto")
        print("5. Remover produto")
        print("6. Listar produtos esgotados")
        print("7. Sair do menu")
        print("==================")

        numero_escolhido = input("Digite uma opção: ")

        if numero_escolhido == "1":
            try:
                descricao = input("Digite a descrição do produto: ")
                codigo = int(input("Digite o código do produto: "))
                quantidade_estoque = int(input("Digite a quantidade em estoque do produto: "))
                custo_item = float(input("Digite o custo do produto: "))
                preco_venda = float(input("Digite o preço de venda do produto: "))
                
                cadastrar_produto(descricao, codigo, quantidade_estoque, custo_item, preco_venda)

            except ValueError:
                print("Erro: Por favor, insira valores numéricos válidos para código, quantidade, custo e preço.")

        elif numero_escolhido == '2':
            listar_produtos()

        elif numero_escolhido == '3':
            tipo_ordenacao = input("Deseja ordenar de que forma? (Digite 'crescente' ou 'decrescente'): ")
            lista_ordenada = ordenar_lista(tipo_ordenacao)
            listar_produtos(lista_ordenada)

        elif numero_escolhido == '4':
            tipo_busca = input("Deseja buscar pela descrição ou código? (Digite 'descrição' ou 'código'): ")
            termo = input("Digite o produto que deseja buscar? ")
            if tipo_busca.lower() == 'descrição':
                buscar_produtos(descricao=termo)
            elif tipo_busca.lower() == 'código':
                buscar_produtos(codigo=termo)
            else:
                print("Digite 'descrição' ou 'código' para realizar a busca")
    
        elif numero_escolhido == '5':
            try:
                produto_a_remover = int(input("Digite o código do produto que deseja remover: "))
                remover_produto(produto_a_remover)
            except ValueError:
                print("Erro: Por favor, insira um código válido.")

        elif numero_escolhido == '6':
            listar_produtos_esgotados()

        elif numero_escolhido == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()

