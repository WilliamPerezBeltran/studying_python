"""funciones de ayuda"""

import os 
import platform 

# platform tiene una funcion llamada system() que me muestra el sistema operativo

def clear():
	if platform.system() == "windows":
		os.system('cls')
	else:
		os.system('clear')