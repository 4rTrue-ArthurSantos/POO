class Pessoa:

    def __init__(self,nome,cpf,altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura

    def exibe_cpf(self):
        return self.cpf

class Secretaria(Pessoa):
    def __init__(self,nome,cpf,altura,id_secretaria):
        super().__init__(nome,cpf,altura)
        self.id_secretaria = id_secretaria 

class Vendedor(Pessoa):
    def __init__(self,nome,cpf,altura,vendas):
        super().__init__(nome,cpf,altura)
        self.vendas = vendas 


sec1 = Secretaria('Maria','124355','170','2')
print(sec1.exibe_cpf())
