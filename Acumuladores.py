""" 
	Ejemplo 2 - ¿Cuándo utilizar un acumulador?
		
		Los acumuladores son variables creadas que nos permiten
		como su nombre lo indica, llevar una ACUMULACIÓN de varios
		resultados. Son utilizados para el calculo de sumatorias,
		el calculo de valores que cumplan una condición en concreta,
		entre otros.  

		Veamos un ejemplo. Realicemos un programa donde el usuario
		ingresará una secuencia de números finalizada en cero (0)
		e indiquemos la SUMA total de los números pares ingresados y
		la SUMA total de los números impares ingresados.
"""

# Inicializamos las variables acumuladoras
acumPares = 0
acumImpares = 0

# Le pedimos al usuario un primer número
numeroIngresado = int(input('Ingrese un número: '))

while numeroIngresado != 0:
	# Verificamos si el número ingresado es par
	if numeroIngresado % 2 == 0:
		# De ser un número par, aumentamos el contador de números pares
		acumPares = acumPares + numeroIngresado
	else:
		# De no ser un número par, entonces, es un número impar
		# y aumentamos el contador de números impares
		acumImpares = acumImpares + numeroIngresado
	# Luego, le pedimos otro número al usuario, hasta que este ingrese un número cero (0)
	numeroIngresado = int(input('Ingrese otro número: '))

# Finalmente, fuera del ciclo While, imprimimos la suma de los números pares e impares.
print('Suma de números pares ingresados: ' + str(acumPares))
print('Suma de números impares ingresados: ' + str(acumImpares))
