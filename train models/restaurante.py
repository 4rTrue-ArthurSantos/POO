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

class Cozinheiro(Funcionario):
    cardapio = ['salada','arroz','sopa','torta']

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)
    
    @classmethod
    def cozinhar(cls,prato):
        if prato in cls.cardapio:
            print(f'O cozinheiro já está preparando {prato}')
        else:
            print(f'{prato} não está disponível no nosso cardápio')




if __name__ == '__main__':
    jorge = Cozinheiro('jorge',27,'R$2500')
    print(jorge.salario)
    jorge.cozinhar('arroz')