class Usuario:
    cargo = 'usuario'

    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def retorna_altura(self):
        print(self.altura)

    @classmethod
    def cargo_usuario(cls):
        cls.cargo = "Gerente"
        print(cls.cargo)

    @staticmethod
    def e_verme(verme):
        if verme == 'fiter':
            return True 


usuario1 = Usuario('arthur',22,1.72)
