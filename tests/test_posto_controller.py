import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.controllers.posto_controller import PostoController

def test_adicionar_posto():
    controller = PostoController()
    controller.adicionar_posto("Posto Teste", 4.0)
    assert len(controller.postos) == 1
    assert controller.postos[0].nome == "Posto Teste"
    assert controller.postos[0].avaliacao == 4.0
