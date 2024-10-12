import PySimpleGUI as sg
susunan = [
  [sg.Text("UNISKA MAB", font=("helvetica", 24))],
  [sg.Text("BANJARMASIN", font=("courier", 20))]
]
window = sg.Window(title="New Icon",
                   layout=susunan,
                   element_justification="center",
                   icon="C:/Users/lenovo/Downloads/favicon.ico", 
                   size=(430, 220))
window.read()
window.close()
