import flet as ft

class MainPage:
    def __init__(self, page):
        self.page = page
        self.value_time = "Minutos"  # Defina o valor inicial como minutos

    def on_change_time(self, e):
        self.value_time = 'Segundos' if self.value_time == 'Minutos' else 'Minutos'
        self.page.clean()
        self.add_elements()

    def add_elements(self):
        self.page.add(
            ft.Column(
                [
                    ft.Switch(
                        value=self.value_time,
                        on_change=self.on_change_time,
                    ),
                    ft.Row(
                        [
                            ft.TextField(
                                label="Tempo:",
                            ),
                    ),
                ]
            )
        )

    def main(self):
        self.page.title = "Desligamento"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.add_elements()

def app_main(page: ft.Page):
    MainPage(page).main()

ft.app(target=app_main)
