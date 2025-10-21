import flet as ft
import json
import os
import sys
import multiprocessing
import atexit

# Отключаем ненужные процессы
if hasattr(multiprocessing, 'set_start_method'):
    multiprocessing.set_start_method('spawn', force=True)

def cleanup():
    """Очистка процессов при выходе"""
    try:
        current = multiprocessing.current_process()
        if current.name == 'MainProcess':
            for process in multiprocessing.active_children():
                process.terminate()
    except:
        pass

# Регистрируем очистку
atexit.register(cleanup)

def main(page: ft.Page):
    # Базовые настройки - УБИРАЕМ все сложные настройки
    page.title = "NetDuty"
    page.window.width = 800
    page.window.height = 600
    page.window.min_width = 600
    page.window.min_height = 400
    
    # Простая навигация
    def show_common(e=None):
        page.clean()
        page.add(common_page)
        page.update()
    
    def show_classes(e=None):
        page.clean()
        page.add(classes_page)
        page.update()
    
    def exit_app(e):
        """Корректный выход"""
        cleanup()
        page.window.close()
        sys.exit(0)
    
    # Простые страницы
    common_page = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Text("NetDuty", size=20, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.CLOSE, on_click=exit_app)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            bgcolor=ft.colors.BLUE_100
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("Добро пожаловать в NetDuty", size=16),
                ft.ElevatedButton("Классы", on_click=show_classes, 
                                style=ft.ButtonStyle(
                                    color=ft.colors.WHITE,
                                    bgcolor=ft.colors.BLUE
                                )),
                ft.Text("Простое приложение для учета дежурств", size=12)
            ], alignment=ft.MainAxisAlignment.CENTER, 
               horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
    ], expand=True)
    
    classes_page = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=show_common),
                ft.Text("Классы", size=20, weight=ft.FontWeight.BOLD),
                ft.Container(width=40)  # placeholder для выравнивания
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            bgcolor=ft.colors.GREEN_100
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("Список классов", size=16),
                ft.Text("Функциональность будет добавлена позже"),
                ft.ElevatedButton("Назад", on_click=show_common)
            ], alignment=ft.MainAxisAlignment.CENTER,
               horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
    ], expand=True)
    
    # Начальная страница
    show_common()

if __name__ == "__main__":
    # Используем простой режим запуска
    try:
        ft.app(
            target=main,
            view=ft.AppView.WEB_BROWSER,
            port=0  # Автовыбор порта
        )
    except KeyboardInterrupt:
        cleanup()
    except Exception as e:
        print(f"Ошибка запуска: {e}")
        cleanup()
