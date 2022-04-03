import PySimpleGUI as sg
import os

# Path and folder name
path = ''
folder = ''


# GUI defination
sg.theme('LightGrey1')

layout = [
	[sg.Text('Enter path',pad=(10,20)),sg.Input(expand_x=True,key="-PATH-")],
	[sg.Text('Enter folder name',pad=(10,20)),sg.Input(expand_x=True,key="-FOLDER-")],
	[sg.Button('Find folders',size=(15,2),pad=(215,20),key="-STORE-")],
	[sg.Listbox(['A'],size=(30,30),expand_x=True,select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE,key="-SELECT-")],
	[sg.Button('Delete',size=(15,2),pad=(215,20),key="-DELETE-")],
]

window = sg.Window('dirkill',layout)


# GUI loop
while True:
	event,values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-STORE-':
		# Gathers our path and folder name
		if values['-PATH-'] and values['-FOLDER-'] != '':
			path = values['-PATH-']
			folder = values['-FOLDER-']
			print(path,folder)
	if event == '-DELETE-':
		if values['-SELECT-'] != []:
			print("Hi for now")

window.close()