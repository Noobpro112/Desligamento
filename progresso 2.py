import flet as ft
import os

class MainPage:
    def __init__(self, page):
        self.page = page
        self.value_time = "Minutos"  # Defina o valor inicial como minutos
        self.time = 0

    def on_change_time(self, e):
        self.value_time = 'Segundos' if self.value_time == 'Minutos' else 'Minutos'
        self.page.clean()
        self.add_elements()

    def on_change_text(self, e):
        self.time = e.target.value

    def add_elements(self):
        switch = ft.Switch(
            value=self.value_time,
            on_change=self.on_change_time,
        )

        text_field = ft.TextField(
            label="Tempo:",
            on_change=self.on_change_text,
        )

        self.page.add(
            ft.Column(
                [
                    switch,
                    ft.Row(
                        [
                            text_field,
                            ft.Text(f" {self.value_time}"),
                        ],
                    ),
                    ft.ElevatedButton(
                        text="Desligar!",
                        on_click=self.shutdown,
                    ),
                ]
            )
        )

    def shutdown(self, e):
        time = self.time
        if self.value_time == 'Minutos':
            time = int(time) * 60
        os.system(f"shutdown /s /t {time}")

    def main(self):
        self.page.title = "Desligamento"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.add_elements()

def app_main(page: ft.Page):
    MainPage(page).main()

ft.app(target=app_main)
