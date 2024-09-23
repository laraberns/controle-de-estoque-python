estoque = []

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

# Cadastro de produtos
def cadastrar_produto(descricao, codigo, quantidade_estoque, custo_item, preco_venda):
    """
    Cadastra um novo produto no estoque.

    Parâmetros:
    descricao (str): Descrição do produto.
    codigo (int): Código único do produto.
    quantidade_estoque (int): Quantidade disponível em estoque do produto.
    custo_item (float): Custo do produto.
    preco_venda (float): Preço de venda do produto.

    Retorna:
    None

    Se o código do produto já existir no estoque, exibe uma mensagem informando que o produto não pode ser cadastrado.
    """
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
    """
    Adiciona produtos iniciais ao estoque a partir de uma string de dados.

    A string de dados é formatada com produtos separados por '#' e atributos de produtos separados por ';'. Cada produto contém a descrição, código, quantidade em estoque, custo e preço de venda.

    Parâmetros:
    None

    Retorna:
    None
    """
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
    """
    Lista os produtos cadastrados no estoque.

    A função imprime no terminal uma tabela com as informações de cada produto, incluindo descrição, código, quantidade em estoque, custo e preço de venda.

    Parâmetros:
    lista_produtos (list, opcional): Uma lista de produtos a ser exibida. Se não for fornecida, usa a lista global `estoque`.

    Retorna:
    None
    """
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
    """
    Ordena a lista de produtos no estoque pela quantidade disponível.

    A função organiza os produtos em ordem crescente ou decrescente com base na quantidade em estoque.

    Parâmetros:
    tipo (str): Um string que indica a ordem de classificação. Deve ser 'crescente' ou 'decrescente'.

    Retorna:
    list: Uma lista ordenada de produtos com base na quantidade em estoque. Se a opção fornecida não for válida, retorna None e exibe uma mensagem de erro.
    """
    if tipo.lower() == "crescente":
        estoque_ordenado = sorted(estoque, key=lambda x: x['quantidade_estoque'])
    elif tipo.lower() == "decrescente":
        estoque_ordenado = sorted(estoque, key=lambda x: x['quantidade_estoque'], reverse=True)
    else:
        return print("Digite 'crescente' ou 'decrescente'")
    return estoque_ordenado

# Busca de Produtos
def buscar_produtos(descricao='', codigo=''):
    """
    Busca produtos no estoque com base na descrição ou código.

    A função procura por produtos que correspondam à descrição fornecida ou ao código do produto. Os produtos encontrados são exibidos na lista.

    Parâmetros:
    descricao (str): A descrição do produto a ser buscado. Se não for fornecida, a busca é feita pelo código.
    codigo (str): O código do produto a ser buscado. Se não for fornecido, a busca é feita pela descrição.

    Retorna:
    None: Exibe a lista de produtos encontrados ou uma mensagem indicando que nenhum produto foi encontrado.
    """
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
    """
    Remove um produto do estoque com base no código fornecido.

    A função procura o produto pelo código e, se encontrado, remove-o do estoque. Uma mensagem é exibida indicando o resultado da operação.

    Parâmetros:
    codigo (int): O código do produto a ser removido do estoque.

    Retorna:
    None: Exibe uma mensagem indicando se o produto foi removido ou não encontrado.
    """
    for produto in estoque:
        if produto['codigo'] == codigo:
            estoque.remove(produto)
            print(f"Produto com código {codigo} removido.")
            return
    print(f"Produto com código {codigo} não encontrado.")

# Consulta de produtos esgotados:
def listar_produtos_esgotados():
    """
    Lista os produtos que estão esgotados no estoque.

    A função verifica todos os produtos no estoque e adiciona aqueles com quantidade em estoque igual a zero a uma lista. Se houver produtos esgotados, eles são exibidos usando a função `listar_produtos`. Caso contrário, uma mensagem é exibida informando que não há produtos esgotados.

    Retorna:
    None: Exibe a lista de produtos esgotados ou uma mensagem informando que não há produtos esgotados.
    """
    produtos_esgotados = [] 
    for produto in estoque:
        if produto['quantidade_estoque'] == 0:
            produtos_esgotados.append(produto)

    if produtos_esgotados:
        listar_produtos(produtos_esgotados)
    else:
        print("Não há produtos esgotados.")

# Filtro de produtos com baixa quantidade:
def filtrar_produtos_pela_quantidade(quantidade = 10):
    """
    Filtra e lista produtos com quantidade em estoque abaixo de um valor especificado.

    A função verifica todos os produtos no estoque e adiciona aqueles com quantidade em estoque inferior ao valor especificado (padrão é 10) a uma lista. Se houver produtos com quantidade baixo do especificado, eles são exibidos usando a função `listar_produtos`. Caso contrário, uma mensagem é exibida informando que não há produtos com quantidade abaixo do limite.

    Parâmetros:
    quantidade (int): O limite de quantidade para filtrar os produtos (padrão é 10).

    Retorna:
    None: Exibe a lista de produtos com quantidade abaixo do limite ou uma mensagem informando que não há produtos com essa quantidade.
    """
    produtos_com_quantidade_abaixa = [] 
    for produto in estoque:
        if produto['quantidade_estoque'] < quantidade:
            produtos_com_quantidade_abaixa.append(produto)

    if produtos_com_quantidade_abaixa:
        listar_produtos(produtos_com_quantidade_abaixa)
    else: 
        print(f"Não há produtos com menos de {quantidade} unidade(s).")

# Atualização de estoque:
def atualizar_estoque(codigo, quantidade):
    """
    Atualiza a quantidade de um produto no estoque.

    A função busca um produto pelo código fornecido e atualiza a quantidade em estoque adicionando o valor especificado. Se a nova quantidade resultar em um estoque negativo, uma mensagem de erro é exibida. Se o produto não for encontrado, uma mensagem informando isso é apresentada.

    Parâmetros:
    codigo (int): O código do produto a ser atualizado.
    quantidade (int): O valor a ser adicionado (ou subtraído) da quantidade atual em estoque.

    Retorna:
    None: Exibe mensagens informando o sucesso ou falha da operação.
    """
    produto_encontrado = False
    for produto in estoque:
        if produto['codigo'] == codigo:
            nova_quantidade = produto['quantidade_estoque'] + quantidade
            if nova_quantidade < 0:
                print("Erro: O estoque não pode ficar negativo.")
                return
            produto['quantidade_estoque'] = nova_quantidade
            print("Estoque do produto atualizado com sucesso.")
            produto_encontrado = True
            break

    if not produto_encontrado:
        print("Produto com o código fornecido não foi encontrado.")

# Atualização de preços:
def atualizar_preco_venda(codigo, preco_venda):
    """
    Atualiza o preço de venda de um produto no estoque.

    A função busca um produto pelo código fornecido e atualiza seu preço de venda com o novo valor especificado. Se o novo preço for menor que o custo do item, uma mensagem de erro é exibida. Se o produto não for encontrado, uma mensagem informando isso é apresentada.

    Parâmetros:
    codigo (int): O código do produto cujo preço de venda será atualizado.
    preco_venda (float): O novo preço de venda a ser definido para o produto.

    Retorna:
    None: Exibe mensagens informando o sucesso ou falha da operação.
    """
    produto_encontrado = False
    for produto in estoque:
        if produto['codigo'] == codigo:
            if preco_venda < produto['custo_item']:
                print("Erro: O preço de venda não pode ser menor que o custo do item.")
                return
            produto['preco_venda'] = float(preco_venda)
            print("Preço de venda do produto atualizado com sucesso.")
            produto_encontrado = True
            break

    if not produto_encontrado:
        print("Produto com o código fornecido não foi encontrado.")

# Calcular valor total do estoque:
def calcular_valor_total_estoque():
    """
    Calcula e exibe o valor total do estoque.

    A função percorre todos os produtos no estoque e calcula o valor total multiplicando a quantidade disponível de cada produto pelo seu preço de venda. Se o estoque estiver vazio, uma mensagem apropriada será exibida.

    Retorna:
    None: Exibe o valor total do estoque ou uma mensagem se o estoque estiver vazio.
    """
    if not estoque:
        print("O estoque está vazio.")
        return

    valor_total = 0.0
    for produto in estoque:
        valor_total += produto['quantidade_estoque'] * produto['preco_venda']
    print(f"O valor total em estoque é R$ {valor_total:.2f}")

# Calcular lucro presumido:
def calcular_lucro_presumido():
    """
    Calcula e exibe o lucro presumido do estoque.

    A função percorre todos os produtos no estoque e calcula o lucro total presumido, considerando a diferença entre o preço de venda e o custo de cada item, multiplicado pela quantidade disponível. Se o estoque estiver vazio, uma mensagem apropriada será exibida.

    Retorna:
    None: Exibe o lucro total presumido do estoque ou uma mensagem se o estoque estiver vazio.
    """
    if not estoque:
        print("O estoque está vazio.")
        return

    lucro_total = 0.0
    for produto in estoque:
        lucro_total += produto['quantidade_estoque'] * (produto['preco_venda'] - produto['custo_item'])
    print(f"O lucro total presumido do estoque é R$ {lucro_total:.2f}")

# Menu interativo
def menu():
    """
    Exibe um menu interativo para gerenciar o estoque de produtos.

    O menu oferece opções para adicionar produtos, listar produtos cadastrados, ordenar produtos pela quantidade, buscar produtos, remover produtos, listar produtos esgotados, filtrar produtos com baixa quantidade, atualizar o estoque, atualizar o preço de venda, calcular o valor total do estoque e calcular o lucro presumido do estoque.

    O usuário pode interagir com o menu até escolher a opção de sair.
    
    Retorna:
    None: O menu é exibido até que o usuário decida sair.
    """
    while True:
        print("\n===== MENU ======")
        print("1. Adicionar novo produto")
        print("2. Listar produtos cadastrados")
        print("3. Ordenar produtos pela quantidade")
        print("4. Buscar produto")
        print("5. Remover produto")
        print("6. Listar produtos esgotados")
        print("7. Filtrar produtos com baixa quantidade")
        print("8. Atualizar o estoque")
        print("9. Atualizar o preço de venda")
        print("10. Calcular valor total do estoque")
        print("11. Calcular lucro presumido do estoque")
        print("12. Sair do menu")
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
            quantidade_a_buscar = input("Digite a quantidade que deseja filtrar (ou pressione Enter para usar o padrão de 10): ")
            if quantidade_a_buscar == "":
                filtrar_produtos_pela_quantidade()
            else:
                try:
                    quantidade_a_buscar = int(quantidade_a_buscar)
                    filtrar_produtos_pela_quantidade(quantidade_a_buscar)
                except ValueError:
                    print("Erro: Por favor, insira uma quantidade válida.")

        elif numero_escolhido == '8':
            try:
                codigo = int(input("Informe o código do produto que deseja ajustar o estoque: "))
                quantidade = int(input("Digite a quantidade a ser adicionada ou removida do estoque: "))
                if quantidade < 0:
                    print("Erro: Não é possível remover mais itens do que o disponível em estoque.")
                else:
                    atualizar_estoque(codigo, quantidade)
            except ValueError:
                print("Entrada inválida: Certifique-se de inserir um código numérico válido e uma quantidade correta.")

        elif numero_escolhido == '9':
            try:
                codigo = int(input("Informe o código do produto para ajustar o preço de venda: "))
                preco_venda = float(input("Digite o novo preço de venda do produto: "))
                if preco_venda <= 0:
                    print("Erro: O preço de venda deve ser maior que zero.")
                else:
                    atualizar_preco_venda(codigo, preco_venda)
            except ValueError:
                print("Entrada inválida: Certifique-se de inserir um código numérico válido e um preço de venda correto.")
        
        elif numero_escolhido == '10':
            calcular_valor_total_estoque()
       
        elif numero_escolhido == '11':
            calcular_lucro_presumido()

        elif numero_escolhido == '12':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()

