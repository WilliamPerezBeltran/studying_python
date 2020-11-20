#!/usr/bin/python -tt
# coding=utf-8
import sys 
import pdb

def names(filename):
	f = open(filename,'r')
	text = f.read()
	pdb.set_trace()
	print(text)
	f.close()

def main():
	names(sys.argv[1])

if __name__ == '__main__':
	main()