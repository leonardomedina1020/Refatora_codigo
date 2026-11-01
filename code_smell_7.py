#acoplador(corrente de mensagens)
#tornar acesso mais facil por meio de metodo
class Pais:
    def __init__(self, nome):
        self.nome = nome


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais


class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

    def obter_pais(self):
        return self.estado.pais.nome


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def obter_pais(self):
        return self.endereco.obter_pais()


class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def obter_pais(self):
        return self.cliente.obter_pais()


def verificar_frete_internacional(pedido):
    pais_destino = pedido.obter_pais()

    if pais_destino != "Brasil":
        print("Sujeito à taxa de importação.")
    else:
        print("Frete nacional padrão.")
