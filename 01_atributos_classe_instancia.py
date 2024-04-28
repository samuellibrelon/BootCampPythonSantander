class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'

aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('Giovanna', 2)

print(aluno_1)
print(aluno_2)