from .medicamento import Medicamento
from .gerenciador import Gerenciador

def limpar_tela(): # 2. Crie a função aqui
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    sistema = Gerenciador()
    
    while True:
        limpar_tela() 
        print("\n--- MENU ---")
        print("1. Adicionar Medicamento")
        print("2. Listar Todos")
        print("3. Excluir Medicamento")
        print("4. Sair")
        

def main():
    sistema = Gerenciador()
    
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar Medicamento")
        print("2. Listar Todos")
        print("3. Excluir Medicamento")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do remédio: ")
            hora = input("Horário (ex: 08:00): ")
            freq = input("Frequência (ex: 8h): ")
            med = Medicamento(nome, hora, freq)
            sistema.adicionar(med)
            print("Medicamento adicionado!")
            input("\nPressione Enter para voltar ao menu")
            
        elif opcao == "2":
            print("\nSua lista:")
            if not sistema.lista:
                print("Nenhum medicamento cadastrado.")
            else:
                for i, m in enumerate(sistema.lista):
                    print(f"{i}. {m['nome']} ({m['horario']}) - {m['frequencia']}")
                    input("\nPressione Enter para voltar ao menu")
                    
        elif opcao == "3":
            if not sistema.lista:
                print("\nSua lista está vazia!")
                continue
            
            print("\n--- REMOVER MEDICAMENTO ---")
            # Exibe a lista para o usuário saber qual número digitar
            for i, m in enumerate(sistema.lista):
                print(f"[{i}] - {m['nome']} ({m['horario']})")
            
            try:
                idx = int(input("\nDigite o número do remédio que deseja excluir: "))
                removido = sistema.excluir(idx)
                
                if removido:
                    print(f"Sucesso: '{removido['nome']}' removido da sua lista.")
                    input("\nPressione Enter para voltar ao menu")
                else:
                    print("Erro: Número não encontrado na lista.")
            except ValueError:
                print("Erro: Você deve digitar um número inteiro.")
            if removido:
                print(f"Medicamento '{removido['nome']}' removido com sucesso!")
            else:
                print("Erro: Número inválido!")
                
                
        elif opcao == "4":
            print("Finalizado")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
    