from classes import Escritor,Caneta,MaquinaDeEscrever

escritor = Escritor('Pedro')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
maquina.escrever()