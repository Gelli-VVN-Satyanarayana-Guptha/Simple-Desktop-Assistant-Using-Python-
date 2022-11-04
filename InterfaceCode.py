from tkinter import font
import PySimpleGUI as sg
from FridayCode import *

sg.theme("SandyBeach")

layout = [

    [sg.Button('F.R.I.D.A.Y',size=(13,2),font=("Italic",20),button_color='black',pad=(165,20))],
    [sg.Text('Input:',font=("Arial",16),pad=(20,3)),sg.InputText(font=('Arial',14),text_color='black',size=(26,10),key = 'inp')],
    [sg.Button('Quit',size=(18,2),pad=(62,20)),sg.Button('Submit',size=(18,2),pad=(42,10))],
    [sg.Text('Output: ',font=("Arial",18),pad=(20,3))],
    [sg.Output(size =(39,12),background_color='white',text_color='darkblue',font=("Times",15),key='op')]

]

fd = sg.Window("VIRTUAL DESKTOP ASSISTANT",layout)

while (True):
    event,values= fd.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    if event == 'F.R.I.D.A.Y':
        try:
            runFriday()
        except Exception as e:
            sg.Print("Some error occured")
    if event == 'Submit':
        None

    fd.FindElement('op').Update('')
    fd.refresh()
    time.sleep(10)
    
fd.close()
