import flet as ft
import json
import os
import sys

def main(page: ft.Page):
    # Только базовые настройки
    page.title = "NetDuty Minimal"
    page.window.width = 800
    page.window.height = 600
    
    # Простая навигация
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
        ft.Text("NetDuty - Common Page"),
        ft.ElevatedButton("Classes", on_click=show_classes)
    ])
    
    classes_page = ft.Column([
        ft.Text("Classes Page"),
        ft.ElevatedButton("Back", on_click=show_common)
    ])
    
    # Начальная страница
    show_common()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
