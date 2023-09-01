class Assinante:

    def __init__(self,nome,idade,ID):
        self.nome = nome
        self.idade = idade
        self.id = ID

    def imprimir_dados(self):
        print(f'{self.nome}\t|\t{self.idade}\t|\t{self.id}')

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,identificador):
        size = len(identificador)
        if size < 8:
            completer = '0'*(8-size)
            identificador = completer + identificador
        self._id = identificador 


user1 = Assinante('Pedro',22,'12')

user1.imprimir_dados()

    