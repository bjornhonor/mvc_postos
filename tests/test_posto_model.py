import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.posto_model import Posto

def test_posto_criacao():
    posto = Posto("Posto Teste", 5.0)
    assert posto.nome == "Posto Teste"
    assert posto.avaliacao == 5.0
