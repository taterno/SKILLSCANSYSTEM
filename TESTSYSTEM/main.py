from settings import *

def main(page: ft.Page):
    page.title = title
    page.theme_mode = theme
    page.window_center()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
        

    def switch_page(e):
        indicator.offset.y = e.control.data
        if e.control.data == 0:
            main.content = homepage
        elif e.control.data == 1:
            main.content = testspage
        elif e.control.data == 2:
            main.content = contactpage
        

        main.update()
        indicator.update()
    
    def start_test(e):
        pass

        
    testspage = ft.Column(
                controls=[
                    ft.Container(
                        bgcolor='#3B3C41',
                        alignment=ft.alignment.top_center,
                        content=ft.Text('Тесты', size=30),
                        border_radius=15                        
                    ),
                    ft.Row(
                        controls=[
                            ft.TextButton('Загрузить тест', style=btnstyledefault),
                            ft.TextButton('Архив тестов', style=btnstyledefault)
                        ]
                    ) 
                ]
            )


    homepage = ft.Column(
                    controls=[
                        ft.Container(
                            bgcolor='#3B3C41',
                            alignment=ft.alignment.top_center,
                            content=ft.Text('Главное меню', size=30),
                            border_radius=15                        
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton('Пройти тест', style=btnstyledefault, expand=True, on_click=start_test),
                            ]
                        ),
                        ft.Container(
                            bgcolor='#3B3C41',
                            alignment=ft.alignment.top_center,
                            content=ft.Text('Список тестов в базе данных', size=15),
                            border_radius=15                        
                        ),
                        #TODO загрузка тестов из базы данных, список
                    ]
                )
        

    contactpage = ft.Column(
                controls=[
                    ft.Container(
                        bgcolor='#3B3C41',
                        alignment=ft.alignment.top_center,
                        content=ft.Text('Связь и тех. поддержка', size=30),
                        border_radius=15                        
                    ),
                    ft.Row(
                        controls=[
                            ft.TextButton('Телеграм', style=btnstyledefault, expand=True)
                        ]
                    ) 
                ]
            )


    main = ft.Container(
            bgcolor='#35363A',
            expand=True,
            height=800,
            alignment=ft.alignment.top_center,
            content=homepage
        )


    mainwindow = ft.Container(
            expand=True,
            bgcolor='#242424',
            content=ft.Row(
                spacing=0,
                controls=[
                    ft.Container(
                        padding=ft.padding.only(top=50),
                        width=40,
                        bgcolor='#242424',
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Column(
                                    expand=True,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    on_click=switch_page,
                                                    expand=True,
                                                    height=34,
                                                    content=ft.Icon(ft.icons.HOME,
                                                                    color=overcolor,
                                                                    tooltip='Главное меню'),
                                                    data=0,
                                                )
                                            ]      
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    on_click=switch_page,
                                                    expand=True,
                                                    height=34,
                                                    content=ft.Icon(ft.icons.CREATE,
                                                                    color=overcolor,
                                                                    tooltip='Тесты'),
                                                    data=1,
                                                )
                                            ]      
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    on_click=switch_page,
                                                    expand=True,
                                                    height=34,
                                                    content=ft.Icon(ft.icons.CONTACT_PAGE,
                                                                    color=overcolor,
                                                                    tooltip='Контакты'),
                                                    data=2,
                                                )
                                            ]      
                                        ),
                                        

                                    ]
                                ),
                                ft.Column(
                                    controls=[
                                        indicator
                                    ]
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor='#303030',
                        expand=True,
                        content=ft.Row(
                            controls=[
                                main,
                                ft.Container(bgcolor='#2C2C2C', expand=True),
                            ]
                        )
                        
                    ),

                ]
            )
        )
    btn = ft.ElevatedButton("quack-quack")

    page.add(mainwindow)
    page.add(btn)


ft.app(target=main, assets_dir="assets", view=ft.FLET_APP_WEB)