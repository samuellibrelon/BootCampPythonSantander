# POO-Herança-múltipla

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self): #código bem útil
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Animal):
    pass

class Gato(Mamifero):
    pass

class Leao(Animal):
    pass

class Ornintorrinco(Mamifero, Ave):
    pass

gato = Gato(nro_patas=4, cor_pelo='Preto')
print(gato)
print()

ornintorrinco = Ornintorrinco(nro_patas = 2, cor_pelo='vermelho', cor_bico='laranja')
print(ornintorrinco)