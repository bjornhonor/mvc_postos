from models.posto_model import Posto
from views.posto_view import PostoView
from typing import List, Optional


class PostoController:
    """Controlador para gerenciar as operações relacionadas aos postos."""

    def __init__(self):
        self.view = PostoView()
        self.postos_mundiais: List[Posto] = self._criar_ranking_mundial()
        self.postos_usuario: List[Posto] = []

    def _criar_ranking_mundial(self) -> List[Posto]:
        """Cria uma lista de postos para o ranking mundial."""
        return [
            Posto("Posto Ipiranga ", 5.0, "Lojas de conveniência am/pm"),
            Posto("Posto Shell", 4.8, "V-Power"),
            Posto("Posto Petrobras", 4.5, "Gasolina Podium"),
            Posto("Posto Ale", 4.0, "Programa de fidelidade vantajoso."),
            Posto("Posto Graal", 3.9, "Postos com serviços completos."),
        ]

    def iniciar(self) -> None:
        """Inicia o loop principal do programa."""
        while True:
            self.view.exibir_menu()
            opcao = self.view.obter_opcao_menu()

            if opcao == 1:
                self.ver_ranking_mundial()
            elif opcao == 2:
                self.ranquear_postos()
            elif opcao == 3:
                self.editar_avaliacoes()
            elif opcao == 4:
                self.visualizar_tabela_usuario()
            elif opcao == 0:
                self.view.exibir_mensagem("xD")
                break
            else:
                self.view.exibir_mensagem("\nOpção inválida. Tente novamente.\n")

    def ver_ranking_mundial(self) -> None:
        """Exibe o ranking mundial de postos."""
        self.view.exibir_ranking_mundial(self.postos_mundiais)
        input("Pressione Enter para retornar ao menu.")

    def ranquear_postos(self) -> None:
        """Permite ao usuário inserir suas avaliações para cada posto."""
        self.postos_usuario.clear()
        for posto in self.postos_mundiais:
            while True:
                avaliacao = self.view.solicitar_avaliacao(posto)
                if avaliacao is not None:
                    novo_posto = Posto(posto.nome, avaliacao, posto.descricao)
                    self.postos_usuario.append(novo_posto)
                    break
        self._ordenar_postos_usuario()
        self.view.exibir_lista_usuario(self.postos_usuario)
        input("\nPressione Enter para retornar ao menu.")

    def editar_avaliacoes(self) -> None:
        """Permite ao usuário editar suas avaliações."""
        if not self.postos_usuario:
            self.view.exibir_mensagem("\n(Você ainda não ranqueou os postos.)")
            return

        self.view.exibir_lista_usuario(self.postos_usuario)
        indice = self.view.solicitar_indice_posto(self.postos_usuario)

        if indice is not None:
            posto_selecionado = self.postos_usuario[indice]
            while True:
                nova_avaliacao = self.view.solicitar_avaliacao(posto_selecionado)
                if nova_avaliacao is not None:
                    posto_selecionado.avaliacao = nova_avaliacao
                    break
            self._ordenar_postos_usuario()
            self.view.exibir_lista_usuario(self.postos_usuario)
            input("\nPressione Enter para retornar ao menu.")

    def visualizar_tabela_usuario(self) -> None:
        """Exibe a tabela de avaliações do usuário."""
        if not self.postos_usuario:
            self.view.exibir_mensagem("\n(Você ainda não ranqueou os postos.)")
            return
        self.view.exibir_lista_usuario(self.postos_usuario)
        input("Pressione Enter para retornar ao menu.")

    def _ordenar_postos_usuario(self) -> None:
        """Ordena a lista de postos do usuário do melhor para o pior."""
        self.postos_usuario.sort(key=lambda posto: posto.avaliacao, reverse=True)