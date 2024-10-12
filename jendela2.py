import PySimpleGUI as sg
window=sg.Window(title="profile",
                 layout=[[sg.Text("NPM          : 2210010485")],
                         [sg.Text("Nama         : RUBEN TRI ARDIAN SAPUTRA")],
                         [sg.Text("Kelas        : 5N")],
                         [sg.Text("Matkull      : pempograman Visual 3")]],
                 size=(400,200))
window()
window.close()