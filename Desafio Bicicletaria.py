# Desafio_Bicicletaria

class Bicicleta: #características da bicicleta
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self): #definindo métodos
        print('TrinTrin...')
    
    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada')

    def correr(self):
        print('Vrummmm...')

    def __str__(self): #código bem útil
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 189)
print(b2)