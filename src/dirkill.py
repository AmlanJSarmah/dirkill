import PySimpleGUI as sg
import os

sg.theme('LightGrey1')

layout = [
	[sg.Text('Enter path',pad=(10,20)),sg.Input(expand_x=True)],
	[sg.Text('Enter folder name',pad=(10,20)),sg.Input(expand_x=True)],
	[sg.Button('Find folders',size=(15,2),pad=(215,20))]
]

window = sg.Window('dirkill',layout)

while True:
	event,values = window.read()

	if event == sg.WIN_CLOSED:
		break

window.close()