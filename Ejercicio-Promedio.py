""" 
	Ejercicio - Sabiendo lo anterior, resolvamos el siguiente ejercicio.

		Realice un programa que permita al usuario ingresar diez (10) números
		e indique el porcentaje de números pares e impares ingresados. 

		Ayuda: Para este ejercicio, debemos llevar un conteo de los números pares
		e impares que ingrese el usuario. Dado a que sabemos que el usuario va a ingresar
		diez (10) números, podemos hacer uso de un ciclo for.

		Este es un detalle IMPORTANTE, cuando no sabemos la cantidad de iteraciones
		(ejemplos anteriores), lo aconsejable es utilizar un ciclo While, en caso contrario, 
		si conocemos la cantidad de iteraciones, lo aconsejable es utilizar un ciclo For. 
"""

# Ya sabemos que serán diez (10) números a ingresar
CANTIDAD_NUMEROS = 10

# Incializamos las variables contadoras
contadorPares = 0
contadorImpares = 0

numeroIngresado = 0 # Podemos inicializarlo en el valor que deseemos

for iteracion in range(CANTIDAD_NUMEROS):
	numeroIngresado = int(input('Ingrese un número: '))
	if numeroIngresado % 2 == 0:
		contadorPares = contadorPares + 1
	else:
		contadorImpares = contadorImpares + 1

# Calculamos el respectivo porcentaje de números pares e impares ingresados
porcentajePares = (contadorPares / CANTIDAD_NUMEROS) * 100
porcentajeImpares = (contadorImpares / CANTIDAD_NUMEROS) * 100

# E imprimimos los valores anteriormente calculados
print('El porcentaje de número pares ingresados es de: ' + str(porcentajePares) + '%')
print('El porcentaje de número impares ingresados es de: ' + str(porcentajeImpares) + '%')