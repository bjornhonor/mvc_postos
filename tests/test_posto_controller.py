import pytest
from src.controllers.posto_controller import PostoController
from src.models.posto_model import Posto


@pytest.fixture
def controller():
    return PostoController()

def test_criar_ranking_mundial(controller):
    postos_mundiais = controller.postos_mundiais
    assert len(postos_mundiais) == 5
    assert isinstance(postos_mundiais[0], Posto)

def test_ver_ranking_mundial(controller, capsys):
    with patch('builtins.input', return_value=''):
        controller.ver_ranking_mundial()
        captured = capsys.readouterr()
        assert "--- Ranking Brasileiro de Postos ---" in captured.out
        # Verifica se os postos foram impressos
        assert "Posto Ipiranga " in captured.out

def test_ranquear_postos(controller, monkeypatch):
    inputs = iter(['4.5', '5.0', '3.8', '4.2', '4.0', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    controller.ranquear_postos()
    assert len(controller.postos_usuario) == 5
    # Verifica se os postos estão ordenados corretamente
    avaliacoes = [posto.avaliacao for posto in controller.postos_usuario]
    assert avaliacoes == sorted(avaliacoes, reverse=True)

def test_editar_avaliacoes_sem_ranqueamento(controller, capsys):
    controller.editar_avaliacoes()
    captured = capsys.readouterr()
    assert "\n(Você ainda não ranqueou os postos.)" in captured.out

def test_editar_avaliacoes(controller, monkeypatch):
    # Primeiro, ranqueamos os postos
    inputs_ranquear = iter(['4.5', '5.0', '3.8', '4.2', '4.0', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_ranquear))
    controller.ranquear_postos()
    
    # Em seguida, editamos a avaliação do segundo posto
    inputs_editar = iter(['2', '4.9', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_editar))
    controller.editar_avaliacoes()
    
    # Verifica se a avaliação foi atualizada
    posto_editado = controller.postos_usuario[0]  # Deve ser o posto com maior avaliação
    assert posto_editado.avaliacao == 4.9
