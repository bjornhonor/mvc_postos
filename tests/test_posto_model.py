
from src.models.posto_model import Posto


def test_criacao_posto():
    nome = "Posto Teste"
    avaliacao = 4.5
    descricao = "Descrição do posto teste."
    posto = Posto(nome, avaliacao, descricao)
    
    assert posto.nome == nome
    assert posto.avaliacao == avaliacao
    assert posto.descricao == descricao

def test_atualizacao_avaliacao():
    posto = Posto("Posto Atualizável", 3.0, "Descrição inicial.")
    novo_valor = 4.7
    posto.avaliacao = novo_valor
    assert posto.avaliacao == novo_valor
