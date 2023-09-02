class Motor:

    def __init__(self,velocidade) -> None:
        self.velocidade = velocidade

    def acelerar(self,valor):
        self.velocidade += valor

    def desacelerar(self,valor):
        self.velocidade -= valor

class Carro:

    def __init__(self,vo=0) -> None:
        self.motor = Motor(vo)
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self,valor):
        if self.ligado:
            self.motor.acelerar(valor)
        else:
            print("O carro está desligado!")

    def desacelerar(self,valor):
        if self.ligado:
            self.motor.desacelerar(valor)
        else:
            print("O carro está desligado!")

    def velocimetro(self):
        print(f"O carro está a {self.motor.velocidade}km/h")


if __name__ == "__main__":
    meu_carro = Carro()
    meu_carro.acelerar(10)
    meu_carro.ligar()
    meu_carro.acelerar(10)
    meu_carro.velocimetro()
