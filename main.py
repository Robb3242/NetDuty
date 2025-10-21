import flet as ft
import os
import sys

def main(page: ft.Page):
    # Базовые настройки
    page.title = "NetDuty"
    page.window.width = 800
    page.window.height = 600
    page.window.min_width = 600
    page.window.min_height = 400
    
    # Отключаем лишние функции Flet
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def show_common(e=None):
        page.clean()
        page.add(common_page)
        page.update()
    
    def show_classes(e=None):
        page.clean()
        page.add(classes_page)
        page.update()
    
    # Простые страницы
    common_page = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Text("NetDuty", size=20, weight=ft.FontWeight.BOLD),
                ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda _: page.window.close())
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=10,
            bgcolor=ft.colors.BLUE_100
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("Добро пожаловать в NetDuty", size=16),
                ft.ElevatedButton("Классы", on_click=show_classes),
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
                ft.Container(width=40)
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
    
    show_common()

if __name__ == "__main__":
    # Используем самый простой запуск
    ft.app(target=main)
