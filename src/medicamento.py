class Medicamento:
    def __init__(self, nome, horario, frequencia):
        self.nome = nome
        self.horario = horario
        self.frequencia = frequencia

    def to_dict(self):
        
        return {
            "nome": self.nome,
            "horario": self.horario,
            "frequencia": self.frequencia
        }

    def __str__(self):
        return f"{self.nome} | Horário: {self.horario} | Frequência: {self.frequencia}"