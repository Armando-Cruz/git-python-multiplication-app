def listTable(base, limit = 10):
	"""
	Muestra la tabla de multiplicar en consola
	Toma dos parametros: base, límite (opcional)
	"""
	for i in range(1, limit + 1):
		print(f'{base} * {i} = {base * i}')

def saveTable(base, limit = 10):
	"""
	Guardar la taba de multiplicar en un archivo de texto
	"""
	contentFile = ''
	for i in range(1, limit + 1):
		# Crea el contenido del archivo
		contentFile += f'{base} * {i} = {base * i}\n'
	try:
		with open(f'files/tabla-{base}.txt', 'w') as file:
			file.write(contentFile)
			print(f'Archivo guardado exitosamente como tabla-{base}')
	except Exception:
		raise Exception('Ocurrió un error al guardar la tabla')