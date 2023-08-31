class Usuario:

    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def retorna_altura(self):
        print(self.altura)


usuario1 = Usuario('arthur',22,1.72)
