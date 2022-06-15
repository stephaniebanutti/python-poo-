class Datas:
    def __init__(self, dia, mes, ano):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def formataData(self):
        print("sua data formatada é: {}/{}/{}".format(self.dia, self.mes, self.ano))


#Corrigir a entrada de valores com zero a esquerda