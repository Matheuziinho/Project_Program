
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        return f"{self.nome} está estudando."


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        return f"{self.nome} está ensinando {self.disciplina}."


# Criando instâncias
aluno1 = Aluno("Carlos", 16, "2023123")
professor1 = Professor("Ana", 35, "Matemática")

# Usando os métodos
print(aluno1.apresentar())
print(aluno1.estudar())
print(professor1.apresentar())
print(professor1.ensinar())
