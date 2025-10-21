import flet as ft
import os
import sys

# ОТКЛЮЧАЕМ АВТОУСТАНОВКУ ДО ИМПОРТА FLET
os.environ["FLET_DISABLE_AUTO_INSTALL"] = "1"
os.environ["FLET_DISABLE_AUTO_IMPORTS"] = "1"

def main(page: ft.Page):
    page.title = "NetDuty"
    page.window.width = 400
    page.window.height = 300
    
    page.add(
        ft.Column([
            ft.Text("NetDuty - No Auto Install", size=20),
            ft.Text("Flet desktop disabled"),
            ft.ElevatedButton("Exit", on_click=lambda _: page.window.close())
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)
