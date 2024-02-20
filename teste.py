import flet as ft
import time
global value_time
value_time = "Segundos"
def main(page: ft.Page):
    page.title = "Desligamento"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def desligar_computador():
    # Obter o valor da caixa de texto
        tempo_str = page.get_control("tempo_texto").value

    # Validar o valor
        try:
            tempo = int(tempo_str)
            if tempo <= 0:
                raise ValueError
        except ValueError:
            print("Valor inválido. Insira um número positivo.")
            return

    # Converter para a unidade correta
        if value_time == "minutos":
            tempo *= 60

    # Definir o tempo de desligamento
        time.sleep(tempo)
        print("Computador desligado!")

# Adicionar um botão para acionar o desligamento
        page.add(ft.ElevatedButton("Desligar!", on_click=desligar_computador))

    def on_change(e):
        global value_time
        value_time = "minutos" if e.control.value else "segundos"
        page.update()
        page.add(
            ft.Column(
            [
                ft.Text(f"Unidade de tempo: {value_time}"),
                ft.Checkbox(
                    value=value_time == "minutos",
                    on_change=on_change,
                    ),
            ],
            ),
        )


    def textbox_changed(e):
        t.value = e.control.value
        t.value += f' {value_time}'
        page.update()

    t = ft.Text()
    tb = ft.TextField(
        label="Seu computador desligara em: ",
        on_change=textbox_changed,
    )

    page.add(tb, t)

    # Botão "Desligar!" no canto inferior da tela:
    btn = ft.ElevatedButton("Desligar!")
    page.add(btn)

ft.app(target=main)
