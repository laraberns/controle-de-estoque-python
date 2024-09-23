# Sistema de Controle de Estoque

Este é um sistema simples de controle de estoque para uma loja de produtos eletrônicos, desenvolvido em Python. Ele permite o cadastro, consulta e atualização de produtos, além da geração de relatórios sobre o estoque e seus valores. O sistema também calcula o lucro presumido com base no custo e preço de venda dos produtos.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- **Cadastro de Produtos:** Permite o cadastro de novos produtos com os atributos: descrição, código, quantidade, custo do item e preço de venda.
- **Inserção Inicial de Estoque:** O estoque inicial é fornecido como uma string que é convertida em uma lista de produtos.
- **Listagem de Produtos:** Exibe uma lista de todos os produtos cadastrados, incluindo suas informações (descrição, código, quantidade, custo e preço de venda).
- **Ordenação por Quantidade:** Permite ordenar os produtos com base na quantidade disponível, de forma crescente ou decrescente.
- **Busca de Produtos:** Permite buscar produtos no estoque por descrição ou código, com parâmetros obrigatórios passados por palavra-chave.
- **Remoção de Produtos:** Permite a remoção de um produto com base no código.
- **Consulta de Produtos Esgotados:** Exibe todos os produtos com quantidade igual a zero.
- **Filtro de Produtos com Baixa Quantidade:** Gera um relatório de produtos com quantidade abaixo de um limite especificado.
- **Atualização de Estoque:** Permite a atualização de quantidades no estoque, incluindo tanto entradas quanto saídas de produtos.
- **Atualização de Preços:** Permite alterar o preço de venda de um produto.
- **Validação de Atualizações:** Garante que a quantidade de produtos não fique negativa e que o preço de venda não seja inferior ao custo.
- **Cálculo do Valor Total do Estoque:** Calcula o valor total do estoque com base na quantidade e preço de venda de cada produto.
- **Cálculo do Lucro Presumido:** Calcula o lucro presumido do estoque com base na diferença entre o preço de venda e o custo multiplicado pela quantidade de cada item.


## Exemplo de Uso

1. Ao iniciar o sistema, o estoque inicial será processado a partir de uma string.
2. O usuário poderá adicionar novos produtos, atualizar preços e quantidades, ou remover produtos do sistema.
3. O sistema permitirá a consulta de produtos com baixo estoque ou esgotados.
4. Relatórios de valor total do estoque e lucro presumido poderão ser gerados.

## Funcionalidades do Menu

O sistema possui um menu interativo, que oferece as seguintes opções:

- **Cadastrar produto**
- **Listar produtos**
- **Buscar produto**
- **Remover produto**
- **Atualizar estoque**
- **Atualizar preços**
- **Relatório de produtos esgotados**
- **Relatório de produtos com baixa quantidade**
- **Calcular valor total do estoque**
- **Calcular lucro presumido**
- **Ordenar produtos por quantidade**

## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/usuario/sistema-estoque.git

2. Execute o script main.py:

   ```bash
   python main.py


