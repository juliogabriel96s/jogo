class Pessoa: 
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá meu nome é {self.nome} eu tenho {self.idade} anos"


pessoa1 = Pessoa("alice", 30)
message = pessoa1.saudacao()
print(message)

pessoa2 = Pessoa(nome='Rodrigo', idade=30)
message = pessoa2.saudacao()
print(message)