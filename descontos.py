class DescontoPorCincoItens(object):
    
    def __init__(self, proximo_desconto) -> None:
        self.__proximo_desconto = proximo_desconto
    
    def calcula(self, orcamento):
        
        if orcamento.total_de_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)
    
class DescontoPorMaiDeQuintosReais(object):
    
    def __init__(self, proximo_desconto) -> None:
        self.__proximo_desconto = proximo_desconto
    
    def calcula(self, orcamento):
        
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)

class SemDesconto(object):
    
    def calcula(self, orcamento):
        return 0