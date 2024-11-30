"""
Módulo posto_model.py

Este módulo define a estrutura base de um posto.
"""


class Posto:
    """Classe que representa um posto de gasolina."""

    def __init__(self, nome: str, avaliacao: float, descricao: str):
        self.nome = nome
        self.avaliacao = avaliacao
        self.descricao = descricao

    def get_nome(self):
        """Função que retorna o nome de um posto"""
        return self.nome

    def get_avaliacao(self):
        """Função que retorna a avaliação de um posto"""
        return self.avaliacao
