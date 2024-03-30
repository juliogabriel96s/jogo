class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} Está amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcego emitem sons ultrassônicos" 
    

morcego = Morcego(nome="Batman")

print(f"nome do morcego:", morcego.nome)
print(f"som do morcego:", morcego.emitir_som())

print(f"morcego amamentando:", morcego.amamentar())
print(f"morcego voando:", morcego.voar())