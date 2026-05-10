import requests


class IBGEService:
    @staticmethod
    def listar_estados():
        """Retorna uma lista de siglas de todos os estados do Brasil"""
        url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            estados = response.json()
            return [estado["sigla"] for estado in estados]
        except Exception:
            return []

    @staticmethod
    def listar_cidades_por_estado(sigla_uf):
        """Retorna os nomes das cidades de um estado específico"""
        # Limpa a sigla para evitar erros de espaços ou letras minúsculas
        uf = sigla_uf.strip().upper()

        base_url = "https://servicodados.ibge.gov.br/api/v1/localidades"
        url = f"{base_url}/estados/{uf}/municipios"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            dados = response.json()

            # O IBGE retorna uma lista de dicionários.
            # Precisamos extrair a chave 'nome' de cada um.
            nomes_cidades = [cidade["nome"] for cidade in dados]

            # Ordena de A-Z para facilitar a leitura no terminal
            nomes_cidades.sort()

            return nomes_cidades
        except Exception as e:
            print(f"Erro ao conectar com a API do IBGE: {e}")
            return []
