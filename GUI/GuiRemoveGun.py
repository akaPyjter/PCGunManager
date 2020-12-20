import PySimpleGUI as sg

import SetOfStringsClass
from GUI import GuiMessageTextDialog


# TODO search
# TODO Resize and aligment

def run_gui(gun_list):
    sg.theme('DarkAmber')
    table_heading = ['index', 'factory', 'model', 'serial number']
    table_data = create_table_data(gun_list)
    window = create_window(table_data, heading=table_heading)
    numbers_of_picked_guns = []

    while True:
        event, values = window.read()
        if event == "Search":
            search_value = values[0]
            run_search(search_value)
        if event == "Delete":
            table_of_lists = values[1]
            index_of_selected_list = table_of_lists[0]
            if len(table_of_lists) > 0:
                picked_index = int(index_of_selected_list)
                picked_gun = table_data[picked_index]
                picked_gun_serial_number = picked_gun[3]
                numbers_of_picked_guns.append(picked_gun_serial_number)
                table_data.remove(picked_gun)
                window = refresh_window(refresh_table_data(table_data), table_heading, window)
            else:
                GuiMessageTextDialog.run_gui("You need to pick expected row")
        if event == "Remove":
            provided_users_index = values[2]
            if is_user_value_correct(provided_users_index) and int(provided_users_index)-1 < len(table_data):
                picked_index = int(provided_users_index) -1
                picked_gun = table_data[picked_index]
                picked_gun_serial_number = picked_gun[3]
                numbers_of_picked_guns.append(picked_gun_serial_number)
                table_data.remove(picked_gun)
                window = refresh_window(refresh_table_data(table_data), table_heading, window)
            else:
                GuiMessageTextDialog.run_gui("Provided value: " + provided_users_index + " is incorrect")
        if event == sg.WIN_CLOSED or event == "Back":
            break
        if len(table_data) == 0:
            GuiMessageTextDialog.run_gui("There are no more guns")
            break

    window.close()
    print(numbers_of_picked_guns)
    return numbers_of_picked_guns


def refresh_table_data(table_data):
    index = 1
    for row in table_data:
        row[0] = index
        index += 1
    return table_data


def create_table_data(gun_list):
    table_data = []
    index = 1
    for gun in gun_list:
        temporary_tab = [index, gun.get_factory(), gun.get_model(), gun.get_number()]
        table_data.append(temporary_tab)
        index += 1
    return table_data


def is_user_value_correct(user_value):
    try:
        int(user_value)
    except (TypeError, ValueError):
        return False
    return True


def create_window(table_data, heading, first_invoke=True):
    return refresh_window(table_data, heading, first_invoke=first_invoke)


def refresh_window(table_data, heading, window=None, first_invoke=False):
    if not first_invoke:
        window.close()
    layout = [[sg.Input("Write gun here"), sg.Button("Search")],
              [sg.Table(values=table_data, auto_size_columns=True, headings=heading), sg.Button('Delete')],
              [sg.Text(SetOfStringsClass.choice_gun), sg.Input('0', size=(3, 1))],
              [sg.Button("Remove"), sg.Button("Back")]
              ]
    window = sg.Window(SetOfStringsClass.program_name, layout, location=(0, 0), element_justification='right')
    return window


def run_search(text):
    pass
