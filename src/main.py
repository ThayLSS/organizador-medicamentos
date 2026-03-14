"""Módulo para gerenciamento de medicamentos via linha de comando."""

class GerenciadorMedicamentos:
    """Classe responsável por gerenciar a lista de medicamentos."""

    def __init__(self):
        """Inicializa o gerenciador com uma lista vazia."""
        self.medicamentos = []

    def adicionar(self, nome, horario, dosagem):
        """Adiciona um novo medicamento à lista."""
        if not nome or not horario:
            return False
        self.medicamentos.append({"nome": nome, "horario": horario, "dosagem": dosagem})
        return True

    def listar(self):
        """Retorna a lista completa de medicamentos."""
        return self.medicamentos

    def remover(self, indice):
        """Remove um medicamento pelo seu índice."""
        if 0 <= indice < len(self.medicamentos):
            return self.medicamentos.pop(indice)
        return None

def main():
    """Função principal que executa a interface de usuário CLI."""
    gerenciador = GerenciadorMedicamentos()

    while True:
        print("\n--- Organização de Medicamentos ---")
        print("1. Cadastrar | 2. Listar | 3. Remover | 4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            horario = input("Horário: ")
            dosagem = input("Dosagem: ")
            if gerenciador.adicionar(nome, horario, dosagem):
                print("Sucesso!")
        elif opcao == '2':
            print("\nLista:", gerenciador.listar())
        elif opcao == '3':
            idx = int(input("Índice para remover: "))
            removido = gerenciador.remover(idx)
            print(f"Removido: {removido}" if removido else "Erro: índice inválido.")
        elif opcao == '4':
            break

if __name__ == "__main__":
    main()
    