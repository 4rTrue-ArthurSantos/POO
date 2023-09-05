class Funcionario:
    def __init__(self,nome,idade,salario):
        self.__nome = nome
        self.idade = idade
        self.salario = salario

    @property
    def nome(self):
        return self.__nome.title()
    
    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self,valor):
        if isinstance(valor,str) and 'R$' in valor:
            valor = valor.replace('R$','')
        self._salario = float(valor)


if __name__ == '__main__':
    funcionario = Funcionario('jorge',27,'R$2500')
    print(funcionario.salario)  