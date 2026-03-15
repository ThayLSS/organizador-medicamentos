import pytest
from src.gerenciador import Gerenciador
import os

def test_sistema_inicia_vazio():
    arquivo_novo = "vazio_teste.json"
    sistema = Gerenciador(arquivo=arquivo_novo)
    
    assert len(sistema.lista) == 0
    
    if os.path.exists(arquivo_novo):
        os.remove(arquivo_novo)

def test_adicionar_medicamento():
    arquivo_teste = "test_temp.json"
    sistema = Gerenciador(arquivo=arquivo_teste)
    
    sistema.adicionar({"nome": "Dipirona", "horario": "08:00"})
    
    assert len(sistema.lista) > 0
    assert sistema.lista[-1]["nome"] == "Dipirona" 
    
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)

    