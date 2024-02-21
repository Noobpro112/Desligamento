import flet as ft

text_unit = True
value_time = 'Minutos'  # Defina o valor inicial como minutos

def main(page: ft.Page):
    page.title = "Desligamento"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_tempo_mudado(valor_texto):
        global tempo_desligamento
        tempo_desligamento = int(valor_texto) * (60 if value_time == 'Minutos' else 1)

    def on_change_time(e):
        global value_time
        value_time = 'Segundos' if value_time == 'Minutos' else 'Minutos'
        page.children[0].children[1].children[0].children[1].text = f" {value_time}"  # Atualize o texto da unidade de tempo

    page.add(
        ft.Column(
            [
                ft.Switch(
                    value=value_time,
                    on_change=on_change_time,
                ),
                ft.Row(
                    [
                        ft.TextField(
                            label="Tempo:",
                            on_change=lambda e: on_tempo_mudado(
                                e.control.value),
                        ),
                        ft.Text(f" {value_time}"),
                    ],
                ),
                ft.ElevatedButton(
                    text="Desligar!",
                ),
            ]
        )
    )

ft.app(target=main)
