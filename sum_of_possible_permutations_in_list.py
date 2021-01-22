
from itertools import permutations

def sum_of_human_list():
	c = [1,2,3] 
	l = list(permutations(c) )
	print (l)
	i = 1
	while(i<len(l)):
		print(sum(l[i]))
		i =i+1

sum_of_human_list()


def sum_of_computer_list():
	c = [1,2] 
	l = list(permutations(c) )
	print (l)
	i = 1
	while(i<len(l)):
		print(sum(l[i]))
		i =i+1

sum_of_computer_list()		

