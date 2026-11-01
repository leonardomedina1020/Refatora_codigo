#descartável(duplicado)
#metodo unico para o que e igual
class ProcessadorFinanceiro:

    def processar_pagamento(self, valor, taxa, tipo):
        if valor > 0:
            valor_com_taxa = valor + (valor * taxa)
            print(f"Processando {tipo}: R$ {valor_com_taxa}")
        else:
            print("Valor inválido")

    def processar_pagamento_credito(self, valor):
        self.processar_pagamento(valor, 0.05, "crédito")

    def processar_pagamento_debito(self, valor):
        self.processar_pagamento(valor, 0.02, "débito")
