#bloater(muitos parametros)
#dividir em classes

class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, valor_diaria, possui_cafe):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria
        self.possui_cafe = possui_cafe


def criar_reserva(hospede, quarto, data_checkin, data_checkout):
    print(f"Reserva criada para {hospede.nome} (CPF: {hospede.cpf})")
    print(f"Quarto {quarto.numero} ({quarto.tipo})")
    print(f"De {data_checkin} até {data_checkout}")

    total_dias = (data_checkout - data_checkin).days
    total = total_dias * quarto.valor_diaria

    if quarto.possui_cafe:
        total += 50 * total_dias

    print(f"Total a pagar: R$ {total}")
