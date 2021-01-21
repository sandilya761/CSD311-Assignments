
from itertools import permutations 
l = list(permutations(range(4))) 
print (l)
i = 1
while(i<len(l)):
	print(sum(l[i]))
	i =i+1

