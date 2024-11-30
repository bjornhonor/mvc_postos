"""
Teste test_posto_controller.py

Testa as operações relacionadas aos postos, incluindo criação, 
leitura, atualização e exclusão.
"""

from unittest.mock import patch
import pytest
from controllers.posto_controller import PostoController
from models.posto_model import Posto


# Utilizo o disable=W0621 para poder usar o fixture do pytest
@pytest.fixture
def retorna_controller():  # pylint: disable=W0621
    """Retorna o controller para facilitar o código"""
    return PostoController()


def test_criar_ranking_mundial(retorna_controller):  # pylint: disable=W0621
    """Função que testa a criação do ranking brasileiro de postos"""
    postos_mundiais = retorna_controller.postos_mundiais
    assert len(postos_mundiais) == 5
    assert isinstance(postos_mundiais[0], Posto)


def test_ver_ranking_mundial(retorna_controller, capsys):  # pylint: disable=W0621
    """Função que testa a visualização do ranking brasileiro"""
    with patch("builtins.input", return_value=""):
        retorna_controller.ver_ranking_mundial()
        captured = capsys.readouterr()
        assert "--- Ranking Brasileiro de Postos ---" in captured.out
        # Verifica se os postos foram impressos
        assert "Posto Ipiranga " in captured.out


def test_ranquear_postos(retorna_controller, monkeypatch):  # pylint: disable=W0621
    """Função que testa o ranking de postos personalizado"""
    inputs = iter(["4.5", "5.0", "3.8", "4.2", "4.0", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    retorna_controller.ranquear_postos()
    assert len(retorna_controller.postos_usuario) == 5
    # Verifica se os postos estão ordenados corretamente
    avaliacoes = [posto.avaliacao for posto in retorna_controller.postos_usuario]
    assert avaliacoes == sorted(avaliacoes, reverse=True)


def test_editar_avaliacoes_sem_ranqueamento(
    retorna_controller, capsys
):  # pylint: disable=W0621
    """Função que testa editar a tabela inexistente do usuário"""
    retorna_controller.editar_avaliacoes()
    captured = capsys.readouterr()
    assert "\n(Você ainda não ranqueou os postos.)" in captured.out


def test_editar_avaliacoes(retorna_controller, monkeypatch):  # pylint: disable=W0621
    """Função que testa editar as avaliações do usuário"""
    # Primeiro, ranqueamos os postos
    inputs_ranquear = iter(["4.5", "5.0", "3.8", "4.2", "4.0", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_ranquear))
    retorna_controller.ranquear_postos()

    # Em seguida, editamos a avaliação do segundo posto
    inputs_editar = iter(["1", "4.9", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_editar))
    retorna_controller.editar_avaliacoes()

    # Verifica se a avaliação foi atualizada
    posto_editado = retorna_controller.postos_usuario[
        0
    ]  # Deve ser o posto com maior avaliação
    assert posto_editado.avaliacao == 4.9
