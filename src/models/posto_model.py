from typing import List

class Posto:
    """Classe que representa um posto de gasolina."""

    def __init__(self, nome: str, avaliacao: float, descricao: str):
        self.nome = nome
        self.avaliacao = avaliacao
        self.descricao = descricao