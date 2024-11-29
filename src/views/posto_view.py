from typing import List
from models.posto_model import Posto

class PostoView:
    def exibir_postos(self, postos: List[Posto]) -> None:
        for posto in postos:
            print(f"Posto: {posto.nome}, Avaliação: {posto.avaliacao}")
