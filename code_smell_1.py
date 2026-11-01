#code smell identificado: uma única função com várias responsabilidades diferentes(bloater)(função longa)
#solução utilizada:dividir em multiplas funções


class GerenciadorDeVendas:

    def calcular_total(self, itens):
        total = 0
        for item in itens:
            total += item['preco'] * item['quantidade']
        return total

    def aplicar_desconto(self, total, cliente):
        if cliente['tipo'] == 'VIP':
            return total * 0.90
        return total

    def processar_pagamento(self, total, metodo_pagamento):
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

    def gerar_relatorio(self, total, cliente):
        relatorio = (
            f"--- Relatório de Venda ---\n"
            f"Cliente: {cliente['nome']}\n"
            f"Total: R$ {total}\n"
        )

        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)

    def processar_venda(self, itens, cliente, metodo_pagamento):
        total = self.calcular_total(itens)
        total = self.aplicar_desconto(total, cliente)
        self.processar_pagamento(total, metodo_pagamento)
        self.gerar_relatorio(total, cliente)

        print("Venda processada com sucesso.")
