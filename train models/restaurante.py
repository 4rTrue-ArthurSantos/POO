class Funcionario:
    def __init__(self,nome,idade,salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome