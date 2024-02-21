import flet as ft
import flet_easy as fs

app = fs.FletEasy(route_init="/flet-easy")

# We add a page
@app.page(route="/flet-easy")
def index_page(data: fs.Datasy):
    page = data.page

    page.title = "Flet-Easy"

    def go_counter(e):
        page.go("/counter")

    return ft.View(
        route="/flet-easy",
        controls=[
            ft.Text("Home page"),
            ft.FilledButton("Go to Counter", on_click=go_counter),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

# We add a second page
@app.page(route="/counter")
def counter_page(data: fs.Datasy):
    page = data.page

    page.title = "Counter"

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def go_home(e):
        page.go("/flet-easy")

    return ft.View(
        route="/counter",
        controls=[
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
            ft.FilledButton("Go to Home", on_click=go_home),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

# We run the application
app.run()