#!/usr/bin/python -tt
# coding=utf-8

# https://es.wikipedia.org/wiki/Sistema_hexadecimal

import pdb
import sys

def hexadecimal_to_decimal(hexadecimal_number='3E0A'):
	return int(hexadecimal_number,16)
	
def main():
	print(hexadecimal_to_decimal())

if __name__=='__main__':
	main()

