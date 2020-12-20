import PySimpleGUI as sg

import SetOfStringsClass

#TODO quit error
#TODO Add Photo
# TODO unikanie dodawanie tych samych broni
def run_gui():
    sg.theme('DarkAmber')
    layout = [[sg.Text(SetOfStringsClass.provide_factory), sg.Input('Gun Factory')],
              [sg.Text(SetOfStringsClass.provide_model), sg.Input('Gun Model')],
              [sg.Text(SetOfStringsClass.provide_gun_number), sg.Input('Gun Serial Number')],
              [sg.Button("Add")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), size=(400, 400))
    while True:
        event, values = window.read()
        if event == "Add":
            break
        if event == sg.WIN_CLOSED or 'Exit':
            break
    window.close()
    return values

