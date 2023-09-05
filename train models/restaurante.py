class Funcionario:
    def __init__(self,nome,idade,salario):
        self.__nome = nome
        self.idade = idade
        self.salario = salario

    @property
    def nome(self):
        return self.__nome
    
    @property
    def salario(self):
        return self.salario

    @salario.setter
    def salario(self,valor):
        if isinstance(valor,str) and 'R$' in valor:
            valor = valor.split('R$','')
        self.salario = float(valor)
        
