#!/usr/bin/python -tt
# coding=utf-8
'''
NOTA IMPORTANTE:

readlines()
convierte cada linea en una posicion de un list ejemplo
si el archivo tiene solo dos paalabras de esta forma 

william 
perez 
 
entonces lo convierte en esta forma 

['william \n', 'perez \n']

'''
import sys 
import pdb
# debugging

def names(filename):
	f = open(filename,'r')
	lines =f.readlines()
	print(lines)
	f.close()
	
def main():
	names(sys.argv[1])

if __name__ == '__main__':
	main()