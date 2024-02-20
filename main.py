import flet as ft
global value_time
value_time = "Segundos"
def main(page: ft.Page):
    page.title = "Desligamento"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    while main == True:
        page.update()

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
    page.update()

    def textbox_changed(e):
        t.value = e.control.value
        t.value += f' {value_time}'
        page.update()
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
