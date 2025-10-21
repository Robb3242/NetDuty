import types
import json,
import os
import sys

os.environ["FLET_DISABLE_AUTO_INSTALL"] = "1"
os.environ["FLET_DISABLE_AUTO_IMPORTS"] = "1"

try:
    from multiprocessing import freeze_support
    freeze_support()
except ImportError:
    pass 

import flet as ft

def main(page: ft.Page):
    page.adaptive = True
    page.padding = 0
    page.theme_mode = "System"

    # Funcrion's

    def initialization():
        if  page.platform_brightness == ft.Brightness.LIGHT:
            theme_button.icon = ft.Icons.LIGHT_MODE
            page.theme_mode = "light"
        else:
            theme_button.icon = ft.Icons.DARK_MODE
            page.theme_mode = "dark"
        
        page.update()

    
    def change_theme(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            e.control.icon=ft.Icons.LIGHT_MODE
            page.update()
        else:
            page.theme_mode = "dark"
            e.control.icon=ft.Icons.DARK_MODE
            page.update()

    def load_duty():
        pass
    
    def change_page(e):
        page.clean()
        page.add(page.pages.get(e.control.data[0]))
        if isinstance(e.control.data[1], types.FunctionType):
            e.control.data[1](e)

        page.update()

    def create_class():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        classes_dir = os.path.join(base_dir, "Classes")

        data = {
        "city": citylocationfield.value,
        "school": schollocationfield.value,
        "class": classfield.value,
        "word": nameclassfield.value
        }

        filename = f"{citylocationfield.value}{schollocationfield.value}{classfield.value}{nameclassfield.value}.json"
        filepath = os.path.join(classes_dir, filename)
        os.makedirs(classes_dir, exist_ok=True)

        try:
            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("Файл успешно создан!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def validate_class(e):
        val_point = 0

        if len(classfield.value)>0:
            if int(classfield.value) > 11:
                classfield.value = "11"
                crcls_statusoutput.value = "Введите реальный номер класса!"
                crcls_statusoutput.height = 20
                crcls_statusoutput.color = "#E74747"
                classfield.update()
                page.update()

            elif int(classfield.value) < 1:
                classfield.value = "1"
                crcls_statusoutput.value = "Введите реальный номер класса!"
                crcls_statusoutput.height = 20
                crcls_statusoutput.color = "#E74747"
                classfield.update()
                page.update()
            
            else:
                crcls_statusoutput.height = 0
                crcls_statusoutput.value = ""
                page.update()

                val_point += 1
        else:
            crcls_statusoutput.value = "Введите класс!"
            crcls_statusoutput.height = 20
            crcls_statusoutput.color = "#E74747"
            page.update()

        if len(nameclassfield.value) < 1:
            crclsnm_statusoutput.value = "Введите название класcа!"
            crclsnm_statusoutput.height = 20
            crclsnm_statusoutput.color = "#E74747"
            page.update()

        else:
            crclsnm_statusoutput.height = 0
            page.update()

            val_point += 1
        
        if len(citylocationfield.value) > 0:
            if len(citylocationfield.value) < 3:
                lcct_statusoutput.value = 'Введите реальный город!'
                lcct_statusoutput.height = 20
                lcct_statusoutput.color = "#E74747"
                page.update()
            
            else:
                lcct_statusoutput.height = 0
                page.update()

                val_point += 1
            
        else:
            lcct_statusoutput.value = 'Введите город!'
            lcct_statusoutput.height = 20
            lcct_statusoutput.color = "#E74747"
            page.update()

        if len(schollocationfield.value) > 0:
            if len(schollocationfield.value) < 3:
                lcsc_statusoutput.value = "Введите реальную школу!"
                lcsc_statusoutput.height = 20
                lcsc_statusoutput.color = "#E74747"
                page.update()

            else:
                lcsc_statusoutput.height = 0
                page.update()

                val_point += 1
        
        else:
            lcsc_statusoutput.value = "Введите название школы!"
            lcsc_statusoutput.height = 20
            lcsc_statusoutput.color = "#E74747"
            page.update()

        if val_point == 4:
            create_class()
            change_page(e)

    def change_week(e):
        pass

    def load_schols(e):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        classes_dir = os.path.join(base_dir, "Classes")

        schol_list.controls.clear()
        schol_list.update()

        for name_scls in os.listdir(classes_dir):
            with open(os.path.join(classes_dir, name_scls), "r", encoding="utf-8") as f:
                scls = json.load(f)

            schol_list.controls.append(
                ft.ResponsiveRow(
                    controls=[
                            ft.Column([
                                ft.TextButton(f"{scls.get('city')} {scls.get('school')} {scls.get('class')}{scls.get('word')}",
                                              on_click=change_page, data=("duty's", None, name_scls)),
                                ft.Container(
                                    ft.Divider()
                                )
                            ]),
                        ], col={"sm": 12, "md": 10, "lg": 8})
                )
        schol_list.update()
        page.update()

    ## // END

    # Variable's
    schol_field = ft.TextField(label="Поиск")

    citylocationfield = ft.TextField(label="Город")
    schollocationfield = ft.TextField(label="Школа")
    classfield = ft.TextField(label="Класс", input_filter=ft.NumbersOnlyInputFilter())
    nameclassfield = ft.TextField(label="Название", 
                                  input_filter=ft.InputFilter(regex_string=r"^[a-zA-Zа-яА-ЯёЁ\s]*$", allow=True))


    schol_list = ft.ListView(expand=True)

    read_dutys = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("День")),
            ft.DataColumn(ft.Text("Дежурный"))
            ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Понедельник")),
                    ft.DataCell(ft.Text(""))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Вторник")),
                    ft.DataCell(ft.Text(""))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Среда")),
                    ft.DataCell(ft.Text(""))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Четверг")),
                    ft.DataCell(ft.Text(""))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Пятница")),
                    ft.DataCell(ft.Text(""))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Суббота")),
                    ft.DataCell(ft.Text(""))
                ]
            ),
        ]
    )

    edit_dutys = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("День")),
            ft.DataColumn(ft.Text("Дежурный"))
            ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Понедельник")),
                    ft.DataCell(ft.TextField(data=0))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Вторник")),
                    ft.DataCell(ft.TextField(data=1))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Среда")),
                    ft.DataCell(ft.TextField(data=2))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Четверг")),
                    ft.DataCell(ft.TextField(data=3))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Пятница")),
                    ft.DataCell(ft.TextField(data=4))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Суббота")),
                    ft.DataCell(ft.TextField(data=5))
                ]
            ),
        ]
    , expand=True)
    week_changer = ft.Container(
        content=ft.ResponsiveRow(
            controls=[ft.Row(
                controls=[
                ft.Text("   "),
                ft.Text("Неделя 1"),
                ft.IconButton(icon=ft.Icons.ARROW_RIGHT, on_click=change_week,
                            data="+1")
            ],col={"sm": 12, "md": 10, "lg": 8})
    ]))

    crcls_statusoutput = ft.Text(size=15, height=0)
    crclsnm_statusoutput = ft.Text(size=15, height=0)
    lcct_statusoutput = ft.Text(size=15, height=0)
    lcsc_statusoutput = ft.Text(size=15, height=0)

    theme_button = ft.IconButton(icon=ft.Icons.LIGHT_MODE, icon_size=15, on_click=change_theme)

    ## // END
    # Page's 
    comon_page = (
            ft.Container(ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Row([
                                    ft.Text("     "),
                                    ft.Text("NetDuty", size=15)
                                ], expand=True),
                                ft.Row([
                                    theme_button,
                                    ft.IconButton(icon=ft.Icons.CLOSE, icon_size=15, on_click=lambda e: sys.exit())
                                ], expand=True, alignment=ft.MainAxisAlignment.END)
                                ]),
                            height=30,
                            expand=True,
                            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
                        ),
                        ft.ResponsiveRow([
                            ft.ListView(controls=[
                            ft.Text(" "),
                            ft.Text("    Выберите опцию", size=25),
                            ft.Text(""),
                            ft.Row([
                                ft.Text("    "),
                                ft.ElevatedButton(text="Классы", icon=ft.Icons.CLASS_,
                                                on_click=change_page, data=("classes", load_schols))
                            ]),
                            ft.Text(""),
                            ft.Row([
                                ft.Text("    "),
                                ft.ElevatedButton(text="Создать класс", icon=ft.Icons.CREATE,
                                                on_click=change_page, data=("create class", None))
                            ])
                    ], expand=True, col={"sm": 12, "md": 10, "lg": 8})])])))
    
    classes_page = (
            ft.Container(ft.Column([
        ft.Container(
                    content=ft.Row([
                        ft.Row([
                            ft.Text("     "),
                            ft.Text("NetDuty", size=15)
                        ], expand=True),
                        ft.Row([
                            ft.IconButton(icon=ft.Icons.EXIT_TO_APP, icon_size=15,
                                            on_click=change_page, data=("common", None))
                        ], expand=True, alignment=ft.MainAxisAlignment.END)
                        ]),
                    height=30,
                    expand=True,
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
        ),
        ft.ResponsiveRow([
            ft.ListView(controls=[
                ft.Text(''),
                ft.Container(
                    ft.TextField(label='Город/Школа/Класс'),
                    padding=5
                ),
                ft.Text(''),
                ft.Container(
                    schol_list,
                    padding=15
                )
            ], expand=True, col={"sm": 12, "md": 10, "lg": 8})])
        ])))

    clscreate_page = (
    ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.Row([
                        ft.Text("     "),
                        ft.Text("NetDuty", size=15)
                    ], expand=True),
                    ft.Row([
                        ft.IconButton(
                            icon=ft.Icons.EXIT_TO_APP,
                            icon_size=15,
                            on_click=change_page, 
                            data=("common", None)
                        )
                    ], expand=True, alignment=ft.MainAxisAlignment.END)
                ]),
                height=30,
                expand=True,
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST 
            ),
            ft.ResponsiveRow([
            ft.ListView(
                controls=[
                    ft.Text(""),
                    ft.Row([
                        ft.Container(
                            content=ft.Divider(color=ft.Colors.SURFACE_TINT),
                            height=5, expand=True
                        ),
                        ft.Text("Местоположение", size=15, color=ft.Colors.SURFACE_TINT),
                        ft.Container(
                            content=ft.Divider(color=ft.Colors.SURFACE_TINT),
                            height=5, expand=True
                        )
                    ]),
                    ft.Container(
                        content=ft.Column([
                    citylocationfield,
                    lcct_statusoutput,
                    schollocationfield,
                    lcsc_statusoutput
                    ]),
                    padding=5),
                    ft.Text(""),
                    ft.Row([
                        ft.Container(
                            content=ft.Divider(color=ft.Colors.SURFACE_TINT),
                            height=5, expand=True
                        ),
                        ft.Text("Класс", size=15, color=ft.Colors.SURFACE_TINT),
                        ft.Container(
                            content=ft.Divider(color=ft.Colors.SURFACE_TINT),
                            height=5, expand=True
                        )
                    ]),
                    ft.Container(
                        content=ft.Column([
                        classfield,
                        crcls_statusoutput,
                        nameclassfield,
                        crclsnm_statusoutput
                        ]),
                        padding=5),
                    ft.Text(''),
                    ft.ElevatedButton("Ок", icon=ft.Icons.CHECK, 
                                      on_click=validate_class, data=("common", None))
                ], 
                expand=True, col={"sm": 12, "md": 10, "lg": 8}
            )])
        ])
        )
    )

    dutys_page = (
        ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Row([
                        ft.Row([
                            ft.Text("     "),
                            ft.Text("NetDuty", size=15)
                        ], expand=True),
                        ft.Row([
                            ft.IconButton(
                                icon=ft.Icons.EXIT_TO_APP,
                                icon_size=15,
                                on_click=change_page, 
                                data=("common", None)
                            )
                        ], expand=True, alignment=ft.MainAxisAlignment.END)
                    ]),
                    height=30,
                    expand=True,
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST 
                ),
                ft.ResponsiveRow([
                    ft.ListView([
                        ft.Container(
                            content=ft.Row([
                                ft.Text("    "),
                                ft.Column([
                                week_changer,
                                edit_dutys
                            ])], alignment=ft.MainAxisAlignment.CENTER)
                        , padding=20)
                    ],
                    col={"sm": 12, "md": 10, "lg": 8}
                    )
                ])
        ]))
    )

    ## END

    page.add(comon_page)
    initialization()
    page.update()

    page.pages = {
        "classes": classes_page,
        "common": comon_page,
        "create class": clscreate_page,
        "duty's": dutys_page
    }


if __name__ == "__main__":
    ft.app(target=main)
    
