class Funcionario:

    def __init__(self,nome,idade,salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def calcular_bonus(self):
        return self.salario*0.1

class Desenvolvedor(Funcionario):

    def __init__(self, nome, idade, salario,linguagem):
        super().__init__(nome, idade, salario)
        self.linguagem = linguagem

    def calcular_bonus(self):
        return super().calcular_bonus() + 500

class Gerente(Funcionario):

    def __init__(self,nome,idade,salario,departamento):
        super().__init__(nome,idade,salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return super().calcular_bonus() + 1000

alef = Desenvolvedor('Alef',21,3000,'python')
bia = Gerente('Bia',27,8000,'marketing')

print(alef.calcular_bonus())
print(bia.calcular_bonus())

