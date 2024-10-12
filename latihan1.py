import PySimpleGUI as sg

sg.theme("DarkRed2")

window = sg.Window(title="Profile",
                   layout=[
                     [sg.Text("NPM        : 2210010485", text_color="blue", background_color="lightblue")],
                     [sg.Text("NAMA      : RUBEN TRI ARDIAN SAPUTRA", text_color="blue", background_color="lightblue")],
                     [sg.Text("KELAS     : 5N REGULER PAGI BANJARMASIN", text_color="blue", background_color="lightblue")],
                     [sg.Text("MATKUL  : PEMROGAMAN VISUAL 3", text_color="blue", background_color="lightblue")]
                   ],
                   size=(400, 200))

window()
window.close()
