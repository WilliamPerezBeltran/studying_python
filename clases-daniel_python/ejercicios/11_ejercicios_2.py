#!/usr/bin/python -tt
# coding=utf-8


"""
2)Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer,n , find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10  characters
 of her infinite string. There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of
 occurrences of a in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .


Sample Input 0

aba
10
Sample Output 0

7

explicacion:

aba aba aba a
se repitio el string  3 veces enteras y un a 
y el numero de a es : 7
"""
"""
string = aba
numero = 10
respueta = 7 
------------------
string = accaca
numero = 15
contar= 'a'
respueta = 
accacaacaccacac
respuesta = 7
"""

def my_funcion(string,numero, contar):
	string_infinito=""
	while len(string_infinito)!=numero:
		string_infinito+=string
	print (string_infinito)






def main():
	string = "aba"
	numero = 10
	contar= 'a'

if __name__=='__main__':
	main()
