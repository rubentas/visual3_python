import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM   : 2210010485 ")],
                            [sg.Text("Nama  : RUBEN TRI ARDIAN SAPUTRA ")],
                            [sg.Text("Kelas : 5N Regular Banjarmasin ")]],
                    size=(400,200),
                    font=("Times", 18))
window()
window.close()