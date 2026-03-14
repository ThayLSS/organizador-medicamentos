import json
import os

class Gerenciador:
    def __init__(self, arquivo="dados.json"):
        self.arquivo = arquivo
        self.lista = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                return json.load(f)
        return []

   
    def adicionar(self, medicamento):
        self.lista.append(medicamento.to_dict())
        self.salvar()

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.lista, f, indent=4)

    def excluir(self, indice):
        if 0 <= indice < len(self.lista):
            removido = self.lista.pop(indice)
            self.salvar() # Importante salvar após remover
            return removido
        return None