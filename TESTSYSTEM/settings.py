import flet as ft 


title = "Функциональная грамотность"
theme = "dark"
overcolor = '#4f5667'


btnstyledefault = ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: '#CECECE',
                        ft.MaterialState.FOCUSED: '#2A409B',
                        ft.MaterialState.DEFAULT: '#E0E6FF',
                    },
                    bgcolor={ft.MaterialState.FOCUSED: '#6A6C77', "": '#494C5A'},)


indicator = ft.Container(bgcolor= overcolor,
                         width=3,
                         height=40,
                         offset=ft.transform.Offset(0, 0)
                        )


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
                            ft.TextButton('Пройти тест', style=btnstyledefault, expand=True)
                        ]
                    ) 
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