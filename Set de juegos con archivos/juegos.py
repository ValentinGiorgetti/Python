def main(args):
	import AhorcadoConFunciones, reversegam, tictactoeModificado, json
	from datetime import datetime
	import PySimpleGUI as sg

	def mostrar_datos():																																																														    # función para mostrar el contenido de "informacion_jugadores.json"
		layout = [[sg.Multiline(key = 'informacion', size = (50, 20))],
							[sg.Button('Salir')]]
		window = sg.Window('Informacion de los jugadores', layout)

		informacion_jugadores = open('informacion_jugadores.json', 'r')																																											
		diccionario_jugadores = json.load(informacion_jugadores)
		informacion_jugadores.close()

		informacion = ''
		for jugador in diccionario_jugadores:
			lista_juegos = diccionario_jugadores[jugador]
			informacion += f'Nombre del jugador: {jugador}\n\n'
			for juego in lista_juegos:
				informacion += str(juego) + '\n'
			informacion += '\n'
		window.Element('informacion').Update(informacion)
		window.Read()
		window.Close()

	informacion_jugadores = open('informacion_jugadores.json', 'r')																																											# leo el archivo y guardo la información en una variable
	diccionario_jugadores = json.load(informacion_jugadores)
	informacion_jugadores.close()

	juegos_disponibles = {'Ahorcado' : AhorcadoConFunciones, 'Ta - Te - Ti' : tictactoeModificado, 'Otello' : reversegam}																# defino los juegos disponibles 
	nombres_juegos = list(juegos_disponibles.keys())

	layout = [[sg.Text('Ingresá tu nombre', justification = 'center'), sg.Input(key = 'nombre', size = (15, 15)), sg.Button('Cargar nombre')],					# defino el layout del menu de juegos
						[sg.Text('Elegí con qué juego querés jugar', justification = 'center'), sg.Listbox(values = nombres_juegos, key = 'lista_juegos', disabled = True, size = (20, 3), enable_events = True)],
						[sg.Button('Jugar', disabled = True, key = 'boton_jugar'), sg.Button('Salir y guardar', key = 'Salir'), sg.Button('Ver datos guardados', key = 'datos_guardados')]]
	window = sg.Window('Menu de juegos', layout)

	while True:																																																																				 	# leo los eventos de la ventana
		event, values = window.Read()
		if (event in (None, 'Salir')):
			break
		if (event == 'Cargar nombre'):
			if (values['nombre'] == ''):
				sg.Popup('Ingresá un nombre válido')
			else:
				nombre = values['nombre']
				window.Element('lista_juegos').Update(disabled = False)
				window.Element('boton_jugar').Update(disabled = False)
				window.Element('nombre').Update(disabled = True)
				window.Element('Cargar nombre').Update(disabled = True)
		if (event == 'boton_jugar'):
			if (values['lista_juegos'] == []):
				sg.Popup('Tenés que seleccionar un juego')
			else:
				window.Element('boton_jugar').Update('Jugando...', disabled = True)
				window.Element('Salir').Update(disabled = True)
				window.Element('lista_juegos').Update(disabled = True)
				juego = values['lista_juegos'][0]
				juegos_disponibles[juego].main()
				window.Element('boton_jugar').Update('Jugar', disabled = False)
				window.Element('Salir').Update(disabled = False)
				window.Element('lista_juegos').Update(disabled = False)
				fecha = datetime.now().strftime('%Y-%m-%d a las %H:%M')
				diccionario_jugadores[nombre] = [{'Juego' : juego, 'Fecha' : fecha}] if not nombre in diccionario_jugadores else diccionario_jugadores[nombre] + [{'Juego' : juego, 'Fecha' : fecha}]
				sg.Popup(f'¡Fin del juego {juego}!')
		if (event == 'datos_guardados'):
			mostrar_datos()
	window.Close()

	informacion_jugadores = open('informacion_jugadores.json', 'w')																																											# guarda la información en el archivo
	json.dump(diccionario_jugadores, informacion_jugadores, indent = 2)
	informacion_jugadores.close()
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
