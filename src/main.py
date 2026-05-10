import os
from .medicamento import Medicamento
from .gerenciador import Gerenciador
from .services import IBGEService  # Importando o serviço da API


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def consultar_ibge():
    limpar_tela()
    print("--- CONSULTAR LOCALIDADES (IBGE) ---")
    print("Buscando estados...")
    estados = IBGEService.listar_estados()

    if not estados:
        print("Erro ao conectar com a API.")
        return

    print(f"Estados: {', '.join(estados)}")
    uf = input("\nDigite a UF para ver cidades (ex: SP): ").upper()

    if uf in estados:
        print(f"Buscando cidades de {uf}...")
        cidades = IBGEService.listar_cidades_por_estado(uf)
        print(f"\nCidades em {uf}:")
        for cidade in cidades[:15]:  # Mostra as 15 primeiras
            print(f"- {cidade}")
        print(f"\nTotal de {len(cidades)} cidades encontradas.")
    else:
        print("UF inválida.")


def main():
    sistema = Gerenciador()

    while True:
        limpar_tela()
        print("\n--- MENU ---")
        print("1. Adicionar Medicamento")
        print("2. Listar Todos")
        print("3. Excluir Medicamento")
        print("4. Sair")
        print("5. Buscar Medicamento")
        print("6. Consultar Localidades (API IBGE)")  # Nova opção

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do remédio: ")
            hora = input("Horário (ex: 08:00): ")
            freq = input("Frequência (ex: 8h): ")
            med = Medicamento(nome, hora, freq)
            sistema.adicionar(med.to_dict())
            print("Medicamento adicionado!")
            input("\nPressione Enter para voltar ao menu")

        elif opcao == "2":
            print("\nSua lista:")
            if not sistema.lista:
                print("Nenhum medicamento cadastrado.")
            else:
                for i, m in enumerate(sistema.lista):
                    nome = m.get("nome", "Sem nome")
                    hora = m.get("horario", "00:00")
                    freq = m.get("frequencia", "Não definida")
                    print(f"{i}. {nome} ({hora}) - {freq}")
            input("\nPressione Enter para voltar ao menu")

        elif opcao == "3":
            if not sistema.lista:
                print("\nSua lista está vazia!")
            else:
                print("\n--- REMOVER MEDICAMENTO ---")
                for i, m in enumerate(sistema.lista):
                    nome = m.get("nome", "Sem nome")
                    hora = m.get("horario", "00:00")
                    print(f"[{i}] - {nome} ({hora})")
                try:
                    idx = int(input("\nDigite o número para excluir: "))
                    rem = sistema.excluir(idx)
                    if rem:
                        n = rem.get("nome", "Medicamento")
                        print(f"Sucesso: '{n}' removido.")
                    else:
                        print("Erro: Número não encontrado.")
                except ValueError:
                    print("Erro: Digite um número inteiro.")
            input("\nPressione Enter para voltar ao menu")

        elif opcao == "5":
            termo = input("Digite o nome do remédio para buscar: ")
            resultados = sistema.buscar(termo)
            if resultados:
                for m in resultados:
                    texto = (
                        f"Encontrado: {m.get('nome', 'Sem nome')} "
                        f"às {m.get('horario', '00:00')}"
                    )
                    print(texto)
            else:
                print("Nenhum medicamento encontrado.")
            input("\nPressione Enter para voltar ao menu")

        elif opcao == "6":
            consultar_ibge()
            input("\nPressione Enter para voltar ao menu")

        elif opcao == "4":
            print("Finalizado.")
            break
        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter para continuar")


if __name__ == "__main__":
    main()
