from typing import List, Optional
from models.posto_model import Posto


class PostoView:
    """Classe responsável pela interface com o usuário."""

    def exibir_menu(self) -> None:
        """Exibe o menu principal."""
        print("\n--- Sistema de Ranking de Postos de Gasolina ---\n")
        print("1. Ver Ranking Mundial de Postos")
        print("2. Ranquear Postos")
        print("3. Editar Avaliações")
        print("4. Visualizar Sua Tabela")
        print("0. Sair\n")

    def obter_opcao_menu(self) -> int:
        """Obtém a opção escolhida pelo usuário no menu."""
        try:
            opcao = int(input("Escolha uma opção: \n"))
            return opcao
        except ValueError:
            print("Opção inválida. Tente novamente.\n")
            return -1

    def exibir_ranking_mundial(self, postos: List[Posto]) -> None:
        """Exibe o ranking mundial de postos."""
        print("\n--- Ranking Brasileiro de Postos ---\n")
        for idx, posto in enumerate(postos, start=1):
            print(f"{idx}. {posto.nome} - Avaliação: {posto.avaliacao}")
            print(f"   Descrição: {posto.descricao}\n")

    def solicitar_avaliacao(self, posto: Posto) -> Optional[float]:
        """Solicita ao usuário que insira uma avaliação para um posto."""
        try:
            avaliacao = float(input(f"\nAvalie o posto '{posto.nome}' (0.0 - 5.0): "))
            if 0.0 <= avaliacao <= 5.0:
                return round(avaliacao, 1)
            else:
                print("Avaliação deve estar entre 0.0 e 5.0.")
                return None
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return None

    def exibir_lista_usuario(self, postos: List[Posto]) -> None:
        """Exibe a lista de postos ranqueados pelo usuário."""
        print("\n--- Sua Tabela de Avaliações ---\n")
        for idx, posto in enumerate(postos, start=1):
            print(f"{idx}. {posto.nome} - Sua Avaliação: {posto.avaliacao}")
            print(f"   Descrição: {posto.descricao}\n")

    def solicitar_indice_posto(self, postos: List[Posto]) -> Optional[int]:
        """Solicita ao usuário que escolha um posto pelo índice."""
        try:
            indice = int(input("\nDigite o número do posto que deseja editar: "))
            if 1 <= indice <= len(postos):
                return indice - 1
            else:
                print("Índice fora do intervalo. Tente novamente.")
                return None
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            return None

    def exibir_mensagem(self, mensagem: str) -> None:
        """Exibe uma mensagem ao usuário."""
        print(mensagem)