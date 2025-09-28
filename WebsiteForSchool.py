from nicegui import ui 

ui.add_head_html("<div dir=ltr>")

with ui.row().classes("w-full justify-center gap-20"):
    ui.label('Sign up ').style('color: #6E93D6; font-size: 200%; font-family :  Open Sans')
with ui.row().classes("w-full justify-center"):
    with ui.column():
        ui.input('full name')
        ui.input(placeholder="Email",validation={"need to contain @gmail.com": lambda value: "@gmail.com" in value})
        ui.input('Password')
    with ui.column():
        ui.label('Gender')
        ui.radio(['Male', 'Female', 'Other'], value='Male')
        with ui.row().classes("gap-700"):
            ui.button('Sign up', on_click=lambda: ui.notify('Click'))
            ui.link('to Login page', 'LoginPage')
ui.run()