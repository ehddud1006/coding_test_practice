import sys
from itertools import permutations 
a = [1,1,1,1]

random_op = list(permutations(a,len(a)))

print(random_op)