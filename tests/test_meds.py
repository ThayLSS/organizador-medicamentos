import os
from src.gerenciador import Gerenciador 

def limpar_arquivo_teste(arquivo):
    if os.path.exists(arquivo):
        os.remove(arquivo)

def test_adicionar_medicamento():
    arquivo = "test_data.json"
    limpar_arquivo_teste(arquivo) 
    
    gerenciador = Gerenciador(arquivo=arquivo) 
    gerenciador.adicionar({"nome": "Dipirona", "horario": "08:00"})
    
    assert len(gerenciador.lista) == 1
    
    limpar_arquivo_teste(arquivo) 

def test_adicionar_invalido():
    gerenciador = Gerenciador(arquivo="test_data.json")
    gerenciador.adicionar({"nome": "", "horario": ""})
    assert len(gerenciador.lista) > 0 

def test_excluir_inexistente():
    gerenciador = Gerenciador(arquivo="test_data.json")
    resultado = gerenciador.excluir(99) 
    assert resultado == None