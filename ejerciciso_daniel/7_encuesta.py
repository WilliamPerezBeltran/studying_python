#!/usr/bin/python -tt
# coding=utf-8


"""
realizar y procesar una encuesta a N estudiantes en donde se les solicita nombre, 
edad, sexo, cantidad de asignaturas que están cursando y carrera 
(ingeniería civil , electronica electrinca, sistemas, industrial, 
psicologigia, veterinaria y economia)
Los resultados requetidos son los siguientes:

a) Número de hombres con menos de 18 años 
b) Número de mujeres con 18  o mas años
c) Edad y carrera del menos de los hombres
d) edad y carrera de la mayor de las mujeres
e) Promedio de signaturas que cursan los estudiantes 
, sin importar sexo , edad ni carrera.

"""
import pdb

def encuesta():
	pass

		
	edad_hombres = []
	edad_mujeres = []
	carrera_hombres = []
	carrera_mujeres = []
	cantidad_asignaturas_mujeres = []
	cantidad_asignaturas_hombre = []

	# val = ''
	validation = True

	while validation:
		sexo = input("digite su genero, m para masculino y f para femenino ")
		if sexo == 'm' or sexo == 'f':
			validation = False

	if sexo == 'm':
		edad_hombres

		validation = True
		while validation:
			edad = input("Ingrese su edad ")
			if edad.isdigit():
				validation = False
		edad_hombres.append(int(edad))

	print(edad_hombres)
	print(edad_hombres)
			






def main():
	encuesta()


if __name__=='__main__':
	main()
