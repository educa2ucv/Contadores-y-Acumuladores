""" 
	Ejemplo 1 - ¿Cuándo utilizar un contador?
		
		Los contadores son variables creadas que nos permiten
		como su nombre lo indica, llevar un CONTEO de las
		ocurrencias de un evento. 

		Veamos un ejemplo. Realicemos un programa donde el usuario
		ingresará una secuencia de números finalizada en cero (0)
		e indiquemos la cantidad de números pares e impares que se
		ingresaron. 
"""

# Inicializamos las variables contadoras
contadorPares = 0
contadorImpares = 0

# Le pedimos al usuario un primer número
numeroIngresado = int(input('Ingrese un número: '))

while numeroIngresado != 0:
	# Verificamos si el número ingresado es par
	if numeroIngresado % 2 == 0:
		# De ser un número par, aumentamos el contador de números pares
		contadorPares = contadorPares + 1
	else:
		# De no ser un número par, entonces, es un número impar
		# y aumentamos el contador de números impares
		contadorImpares = contadorImpares + 1

	# Luego, le pedimos otro número al usuario, hasta que este ingrese un número cero (0)
	numeroIngresado = int(input('Ingrese otro número: '))

# Finalmente, fuera del ciclo While, imprimimos la cantidad de números pares e impares.
print('Cantidad de números pares ingresados: ' + str(contadorPares))
print('Cantidad de números impares ingresados: ' + str(contadorImpares))