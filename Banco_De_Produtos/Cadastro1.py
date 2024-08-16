from main import Produto
import json
class Estoque(Produto):
    def __init__(self):
        self.id_counter = 0
        self.produtos = []
    def criar(self, nome, marca, categoria, qtd_estoque, preco, desc, fornecedor):
        Produto = Produto(self.id_counter, nome, marca, categoria, qtd_estoque, preco, desc, fornecedor)
        self.id_counter += 1
        id = self.id_counter


        self.produtos.append({
            "id": id,
            "nome": nome,
            "marca": marca,
            "categoria": categoria,
            "qtd_estoque": qtd_estoque,
            "preco": preco,
            "desc": desc,
            "fornecedor": fornecedor
        })
    #adicionar = criar(input("Nome: "), input("Marca: "), input("Categoria: "), int(input("Quantidade em estoque: ")), float(input("Preço: ")), input("Descrição: "), input("Fornecedor: "))
        retry = bool
        if retry:
            try:
                with open("estoque.json", "w") as file:
                    json.dump(self.produtos, file, indent=4)
            except FileNotFoundError:
                print("Arquivo não encontrado")
                retry = True
        else:
            print("Arquivo salvo com sucesso")
            retry = False
        
estoque = Estoque()


    