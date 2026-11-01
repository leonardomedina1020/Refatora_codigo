#impedidor de mudança(divergente)
#separar responsabilidades

class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco


class CalculadoraImposto:
    def calcular_preco_com_imposto(self, produto):
        return produto.preco * 1.15


class BancoDeDados:
    def salvar(self, produto):
        print(f"INSERT INTO produtos (id, nome, preco) VALUES ({produto.id_produto}, '{produto.nome}', {produto.preco});")


class ExportadorXML:
    def exportar(self, produto):
        return f"<produto><id>{produto.id_produto}</id><nome>{produto.nome}</nome><preco>{produto.preco}</preco></produto>"