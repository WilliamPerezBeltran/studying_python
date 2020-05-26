
"""
el metodo listdir del modulo os se llama asi : os.listdir(le envio un path)
le envio un path como argumento y lo que retorna son todos los nombres de los 
archivos que hay en ese path 

nota 
obvimante el path que le envio lo hago con los argumentos de la consola
y se lo envio de esta forma 
 python2 utilities1.py ./
"""

"""
esta es la forma de triglearlo en la consola 
python2 4_getstatusoutput.py .
python2 4_getstatusoutput.py .
python2 4_getstatusoutput.py .
python2 4_getstatusoutput.py .
"""


import sys 
import os 
import commands


def List(dir):
	# cmd hace enfasis a comand or comando
	cmd = 'ls -l ' + dir
	(status,output) = commands.getstatusoutput(cmd)
	print output


def main():
	List(sys.argv[1])
if __name__ == '__main__':
	main()
