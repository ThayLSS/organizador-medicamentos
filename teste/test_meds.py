from src.main import GerenciadorMedicamentos

def test_adicionar_medicamento():
    gerenciador = GerenciadorMedicamentos()
    resultado = gerenciador.adicionar("Dipirona", "08:00", "500mg")
    assert resultado == True
    assert len(gerenciador.listar()) == 1

def test_adicionar_invalido():
    gerenciador = GerenciadorMedicamentos()
    
    resultado = gerenciador.adicionar("", "08:00", "500mg")
    assert resultado == False
    assert len(gerenciador.listar()) == 0

def test_remover_inexistente():
    gerenciador = GerenciadorMedicamentos()
    resultado = gerenciador.remover(99) 
    assert resultado == None