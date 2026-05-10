import pytest
from src.services import IBGEService


def test_conexao_api_ibge_estados():
    estados = IBGEService.listar_estados()
    assert isinstance(estados, list)
    assert "SP" in estados  # Verifica se São Paulo está na lista
    assert len(estados) > 0


def test_conexao_api_ibge_cidades():
    cidades = IBGEService.listar_cidades_por_estado("RJ")
    assert "Rio de Janeiro" in cidades
    assert len(cidades) > 0
