

class MinhaClasse:
    valor = 10
    def __init__(self, nome) -> None:
        self.nome = nome
    def metodo_instancia(self):
        return f"Metodo de instancia chamado para {self.valor}"
    @classmethod
    def metodo_classe(cls):
        return f"Metodo da classe chamado para valor= {cls.valor}"
    @staticmethod
    def metodo_estatico():
        return "Metodo estatico chamado"

obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
         marca, modelo, ano = configuracao.split(",")
         return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,corola,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca {carro1.marca}\nModelo {carro1.modelo}\nAno {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a=10, b=15))