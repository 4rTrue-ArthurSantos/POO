from classes3 import Cliente,Endereco

cliente1 = Cliente('Felipe',34)
cliente1.insere_endereco('Belo Horizonte','MG')
cliente1.lista_enderecos()
print()

del cliente1
print()

cliente2 = Cliente('Maria',27)
cliente2.insere_endereco('Salvador','BA')
cliente2.insere_endereco('Rio de Janeiro','RJ')
cliente2.lista_enderecos()
print()

del cliente2