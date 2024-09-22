
estoque = {}

# Cadastro de produtos
def cadastrar_produto(descricao, codigo, quantidade_estoque, custo_item, preco_venda):

    if codigo in estoque:
        print(f"Produto com o código {codigo} já existe.")
        return

    novo_produto = {
        'descricao': descricao,
        'quantidade_estoque': quantidade_estoque,
        'custo_item': custo_item,
        'preco_venda': preco_venda
    }

    estoque[codigo] = novo_produto
    print(f"Produto com o código {codigo} adicionado com sucesso!")
    return novo_produto

cadastrar_produto("Notebook Dell", 201, 15, 3200.00, 4500.00) 
print(estoque)