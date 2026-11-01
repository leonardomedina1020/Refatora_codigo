#bloater(muitos parametros)
#dividir dados em classes


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


class Contato:
    def __init__(self, ddd, telefone_numero):
        self.ddd = ddd
        self.telefone_numero = telefone_numero


class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, contato):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.contato = contato

    def exibir_dados(self):
        print(f"Funcionário: {self.nome} - {self.cargo}")
        print(f"Contato: ({self.contato.ddd}) {self.contato.telefone_numero}")
        print(f"Endereço: {self.endereco.rua}, {self.endereco.numero} - {self.endereco.bairro}, {self.endereco.cidade}/{self.endereco.estado} - CEP: {self.endereco.cep}")


endereco = Endereco("Rua A", 100, "Centro", "São Paulo", "SP", "01000-000")
contato = Contato(11, "99999-9999")

funcionario = Funcionario("João", "Analista", 3000, endereco, contato)
funcionario.exibir_dados()
