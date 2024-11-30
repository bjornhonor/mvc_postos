"""
Teste test_posto_model.py

Testa o método construtor de model
com a criação de posto e atualização de avaliação.
"""

from models.posto_model import Posto


def test_criacao_posto():
    """Função que testa a criação de um posto"""
    nome = "Posto Teste"
    avaliacao = 4.5
    descricao = "Descrição do posto teste."
    posto = Posto(nome, avaliacao, descricao)

    assert posto.nome == nome
    assert posto.avaliacao == avaliacao
    assert posto.descricao == descricao


def test_atualizacao_avaliacao():
    """Função que testa a atualização de uma avaliação"""
    posto = Posto("Posto Atualizável", 3.0, "Descrição inicial.")
    novo_valor = 4.7
    posto.avaliacao = novo_valor
    assert posto.avaliacao == novo_valor
