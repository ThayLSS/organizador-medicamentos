import requests


class IBGEService:
    @staticmethod
    def listar_estados():

        url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            estados = response.json()
            return [estado["sigla"] for estado in estados]
        except requests.exceptions.RequestException:
            return []

    @staticmethod
    def listar_cidades_por_estado(sigla_uf):

        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_uf}/municipios"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            cidades = response.json()
            return [cidade["nome"] for cidade in cidades]
        except requests.exceptions.RequestException:
            return []
