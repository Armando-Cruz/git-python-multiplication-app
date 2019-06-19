from multiplicar import listTable, saveTable

def showMenu():
	print('=======================================================')
	print('\t\t\t\tApp de Multiplicar')
	print('1. Mostrar Tabla')
	print('2. Guardar Tabla en archivo')
	print('=======================================================')
	

showMenu()
option = input('Opción: ')
while (option != '1') and (option != '2'):
	option = input('Opción: ')

base = int(input('Base: '))
limit = int(input('Multiplicar hasta: '))
try:
	if (option == '1'):
		listTable(base, limit)
	else:
		saveTable(base, limit)
except Exception:
	print('Ha ocurrido un error')