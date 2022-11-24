class ISS(object):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class IOF(object):
    
    def calcula(self, orcamento):
        return orcamento.valor * 6.38