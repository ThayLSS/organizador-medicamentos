import requests


class IBGEService:
    @staticmethod
    def listar_estados():
        url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            dados = response.json()
            return [estado["sigla"] for estado in dados]
        except Exception as e:
            print(f"Erro ao conectar com a API do IBGE: {e}")
            return []

    @staticmethod
    def listar_cidades_por_estado(sigla_uf):
        uf = sigla_uf.strip().upper()

        base = "https://servicodados.ibge.gov.br/api/v1/localidades"
        url = f"{base}/estados/{uf}/municipios"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            dados = response.json()
            # Retorna lista de nomes (ex: 'Rio de Janeiro')
            return [cidade["nome"] for cidade in dados]
        except Exception as e:
            print(f"Erro ao conectar com a API do IBGE: {e}")
            return []
