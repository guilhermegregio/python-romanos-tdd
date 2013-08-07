
def toRomanos(valor):

	result = []
	romanos = [
		{
			0: '',
			1: 'I',
			2: 'II',
			3: 'III',
			5: 'V',
			10: 'X'
		},
		{
			0: '',
			1: 'X',
			2: 'XX',
			3: 'XXX',
			5: 'L',
			10: 'C'
		},
		{
			0: '',
			1: 'C',
			2: 'CC',
			3: 'CCC',
			5: 'D',
			10: 'M'
		},
		{
			0: '',
			1: 'M',
			2: 'MM',
			3: 'MMM'
		}
	]

	numeros = [1000, 500, 100, 50, 10, 5, 1]

	valor = list(str(valor))[::-1]

	for pos in range(len(valor)):
		if valor[pos] == '0':
			continue

		for numero in numeros:
		 	sub = int(valor[pos]) - numero
		 	if sub == -1:
		 		result.append(romanos[pos][1] + romanos[pos][numero])
		 		break
		 	elif sub >= 0:
		 		result.append(romanos[pos][numero] + romanos[pos][sub])
		 		break

	return ''.join(result[::-1])