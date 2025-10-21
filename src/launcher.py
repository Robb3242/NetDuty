import os
import sys
import multiprocessing

# Отключаем multiprocessing ДО импорта flet
os.environ["FLET_DISABLE_MULTIPROCESSING"] = "1"

# Критически важно для Windows
if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    # Добавляем путь к текущей директории
    sys.path.insert(0, os.path.dirname(__file__))
    
    # Импортируем и запускаем основное приложение
    from main import main
    import flet as ft
    
    ft.app(target=main)
