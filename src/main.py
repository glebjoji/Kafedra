"""
Точка входа в приложение. Создает MainController и запускает MVC.
"""

from src.controllers.main_controller import MainController

if __name__ == "__main__":
    app = MainController()
    app.run()
