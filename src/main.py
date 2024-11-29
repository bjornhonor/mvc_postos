from controllers.posto_controller import PostoController

def main() -> None:
    controller = PostoController()
    controller.adicionar_posto("Posto A", 4.5)
    controller.adicionar_posto("Posto B", 3.8)
    controller.mostrar_postos()

if __name__ == "__main__":
    main()
