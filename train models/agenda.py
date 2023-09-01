class Contato:

    def __init__(self,nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
class Agenda:

    def __init__(self):
        self.contatos = []

    def adiciona_contato(self,contato):
        self.contatos.append(contato)

    def remove_contato(self,nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)    
                return f'Contato {nome} removido'
        return f'esse contato não existe na agenda'
    
    def listar_contatos(self):
        for contato in self.contatos:
            print(f'Nome: {contato.nome}, telefone: {contato.telefone}, email: {contato.email}')


arthur = Contato('Arthur','XXXX-XXXX','abc@gmail.com')
bernardo = Contato('Bernardo','YYYY-YYYY','def@gmail.com') 

meus_contatos = Agenda()
meus_contatos.adiciona_contato(arthur)
meus_contatos.adiciona_contato(bernardo)
meus_contatos.listar_contatos()
print(meus_contatos.remove_contato('Arthur'))
meus_contatos.listar_contatos()