class Calculadora:

    @staticmethod
    def soma(a,b):
        return a + b
    
    @staticmethod
    def subtracao(a,b):
        return a-b
    
    @staticmethod
    def multiplicacao(a,b):
        return a*b
    
    @staticmethod
    def divisao(a,b):
        return a/b
    
cassio = Calculadora()

print(cassio.soma(1,3))
print(cassio.divisao(3,2))