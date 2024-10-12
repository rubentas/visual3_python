import PySimpleGUI as sg
sg.theme("DarkGreen4")

window = sg.Window(title="Profile",
                   layout=[
                     [sg.Text("NPM        :2210010485")],
                     [sg.Text("NAMA      :RUBEN TRI ARDIAN SAPUTRA")],
                     [sg.Text("KELAS     :5N REGULER PAGI BANJARMASIN")],
                     [sg.Text("MATKUL  :PEMROGAMMAN VISUAL 3")]
                   ],
                   size=(400, 200))
window()
window.close()
