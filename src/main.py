"""Módulo principal do sistema de ranking de postos de gasolina."""

from controllers.posto_controller import PostoController

def main() -> None:
    """Função principal que inicia o programa."""
    controller = PostoController()
    controller.iniciar()


if __name__ == "__main__":
    main()