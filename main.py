estoque = []

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


cadastrar_produto("Notebook Dell", 201, 15, 3200.00, 4500.00)
cadastrar_produto("Notebook Lenovo", 201, 10, 2800.00, 4200.00) 
cadastrar_produto("Mouse Logitech", 202, 50, 70.00, 150.00)
