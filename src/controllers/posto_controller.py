from typing import List
from models.posto_model import Posto
from views.posto_view import PostoView

class PostoController:
    def __init__(self):
        self.view = PostoView()
        self.postos: List[Posto] = []

    def adicionar_posto(self, nome: str, avaliacao: float) -> None:
        posto = Posto(nome, avaliacao)
        self.postos.append(posto)

    def mostrar_postos(self) -> None:
        self.view.exibir_postos(self.postos)
