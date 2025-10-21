import flet as ft
import sys

# Отключаем все возможные автоимпорты
import os
os.environ["FLET_DISABLE_AUTO_IMPORTS"] = "1"

def main(page: ft.Page):
    page.title = "NetDuty Simple"
    page.window.width = 400
    page.window.height = 300
    
    page.add(
        ft.Column([
            ft.Text("NetDuty - Simple Test", size=20),
            ft.Text("Testing process isolation"),
            ft.ElevatedButton("Exit", on_click=lambda _: page.window.close())
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    # Максимально простой запуск
    ft.app(target=main, view=ft.AppView.FLET_APP)
