from descontos import DescontoPorCincoItens, DescontoPorMaiDeQuintosReais, SemDesconto

class CalculadorDeDescontos(object):
    
    def calcula(self, orcamento):
        
        desconto = DescontoPorCincoItens(
            DescontoPorMaiDeQuintosReais(
                SemDesconto()
            )
        ).calcula(orcamento)
        
        return desconto


if __name__ == "__main__":
    from orcamento import Orcamento, Item
    
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))
    
    calculador = CalculadorDeDescontos()
    desconto_calculado = calculador.calcula(orcamento)
    print(orcamento.valor - desconto_calculado)