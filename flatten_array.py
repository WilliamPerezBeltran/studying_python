x = [1, [2, [3, [4, 5]]]]
# x = [1, 20,[2, [3, [4, 5]]]]

# [1, [2, [3, [4, 5]]]]
# [2, [3, [4, 5]]]
# [3, [4, 5]]
# [4, 5]

# new_array = []
# def flatten(x):
# 	if len(x) != 0:
# 		for a in x:
# 			if isinstance(a,list):
# 	  			flatten(a)
# 			else:				
# 				new_array.append(a)
	  			
# print(new_array)
# flatten(x)
# print(new_array)


class Flatten:
	def __init__(self, x):
		self.empty_list = x

	def flatten_list(self, x):         
		if len(x) != 0:
			for a in x:
				if isinstance(a,list):
					self.flatten_list(a)
				else:	
					self.empty_list.append(a)
def main():
	y = Flatten([])
	y.flatten_list([1, [2, [3, [4, 5]]]])
	print(y.empty_list)


	b = Flatten([])
	b.flatten_list([1, 2,3,4])
	print(b.empty_list)


	c = Flatten([])
	c.flatten_list([1, [2, 34,2,3,[3, [4, 5]]]])
	print(c.empty_list)


	a = Flatten([])
	a.flatten_list([1, [2,32 ,34,[3, [4, 5]]]])
	print(a.empty_list)


	t = Flatten([])
	t.flatten_list([1, 2])
	print(t.empty_list)

if __name__=='__main__':
	main()

