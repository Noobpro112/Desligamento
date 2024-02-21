import flet as ft


def main(page: ft.Page):

    class ExtraParameters(ft.UserControl): # Add a control to the Column
        def __init__(self):
            super().__init__()
            self.Box = ft.Column([])

        def build(self):
            return self.Box

        def addParameterInput(self, key):
            fileTextField = ft.TextField(
                label=key, border=ft.InputBorder.UNDERLINE, hint_text="Select or input full path")
            fileTextField.on_focus = lambda _: getFileDialog(fileTextField)
            fileTextField.prefix =ft.Container(ft.FilledTonalButton("Select",icon = ft.icons.FILE_OPEN, on_click=lambda _:getFileDialog(fileTextField)))
            self.Box.controls.append(fileTextField)
            self.update()

    class ParameterCard(ft.UserControl):  # Cards for users to click
        def __init__(self, title, description, callback, type='text'):
            super().__init__()
            self.title = title
            self.description = description
            self.callback = callback
            self.type = type

        def build(self):
            return ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                title=ft.Text(self.title),
                                subtitle=ft.Text(self.description),
                            ),
                        ]
                    ),
                    on_click=lambda _: self.callback.addParameterInput(
                        self.title),
                    width=400,
                    padding=10,
                )
            )

    def getFileDialog(targetTextField): 
        get_input_file_dialog.pick_files(allow_multiple=False)
        get_input_file_dialog.targetTextField = targetTextField

    def get_input_file_result(e: ft.FilePickerResultEvent):
        e.control.targetTextField.value = e.files[0].path if e.files else "Cancelled!"
        e.control.page.update() # <---- TextField not updated

    get_input_file_dialog = ft.FilePicker(on_result=get_input_file_result)

    fileTextField = ft.TextField(label="This one works", border=ft.InputBorder.UNDERLINE, prefix=ft.Container(ft.Icon(ft.icons.FILE_OPEN), on_click=lambda _: getFileDialog(
        fileTextField)), hint_text="Select file", on_focus=lambda _: getFileDialog(fileTextField)) # This one works


    extra_parameters = ExtraParameters() # But ones in the Column do not work
    
    col = ft.Column([
        fileTextField
    ])

    page.add(get_input_file_dialog, col, extra_parameters, ParameterCard(
        "Add file", 'Click card to add a new line', extra_parameters))


ft.app(target=main)