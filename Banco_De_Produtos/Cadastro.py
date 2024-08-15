from main import Produto

class Estoque(Produto):
    def __init__(self):
        self.id_counter = 0

    def create(self, nome, marca, categoria, qtd_estoque, preco, desc, fornecedor):
        produto = Produto(self.id_counter, nome, marca, categoria, qtd_estoque, preco, desc, fornecedor)
        self.id_counter += 1
        id = self.id_counter
        with open ('arquivo.txt', 'a') as file:
            file.write(f"{id} | {produto.nome}| {produto.marca} | {produto.categoria} | {produto.qtd_estoque} | {produto.preco} | {produto.desc} | {produto.fornecedor} ")



estoque = Estoque()

# Criar um produto usando o método create
estoque.create('Produto A', 'Marca A', 'Categoria A', 10, 99.99, 'Descrição do Produto A', 'Fornecedor A')


                                        

        