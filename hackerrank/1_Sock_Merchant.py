import pdb

"""
John works at a clothing store. He has a large pile of socks that he must pair 
by color for sale. Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

For example, there are  n =7 socks with colors ar=[,1,2,1,2,1,3,2]. There is one 
pair of color 1 and one of color 2. There are three odd socks left, one of each color. 
The number of pairs is  2.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer 
representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in ar .
The second line contains  space-separated integers describing the colors  ar[i]
of the socks in the pile.

Constraints
1<= n <= 100
1<= ar[i] <= 100 where 1<= i <= 100  

Output Format
Return the total number of matching pairs of socks that John can sell.

Sample Input

n = 9
ar =[10 20 20 10 10 30 50 10 20]
Sample Output
3
debe dar 3. 3 es el resultado
"""



def william(n,ar):

	arr_true = [False for x in range(n)]
	result = 0

	for x in range(n):
		for y in range(n):
			# pdb.set_trace()
			# print(x)
			if ar[x] == ar[y] and x != y :
				# pdb.set_trace()
				if arr_true[x] != True and arr_true[y] != True:
					arr_true[x] = True
					arr_true[y] = True
					result+=1
					print("posicion x: %d, posicion y: %d"%(x,y))
					print(arr_true)
					break
					# pdb.set_trace()
			
	print(arr_true)

	return result






print(william(9,[10,20,20,10,10,30,50,10,20]))