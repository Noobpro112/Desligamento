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
        print(f"e: {e}")  # Imprima e
        try:
            self.time = int(e.control.value)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

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
        if time > 0:
            if self.value_time == 'Minutos':
                time = int(time) * 60
            print(f"Tempo para desligamento: {time} segundos")
            os.system(f'shutdown -s -t {time}')
        else:
            print("Por favor, insira um tempo maior que 0.")

    def main(self):
        self.page.title = "Desligamento"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.add_elements()


def app_main(page: ft.Page):
    MainPage(page).main()


ft.app(target=app_main)
