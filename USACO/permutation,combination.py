#permutation
from itertools import permutations
a = ['+','*','/', '-']
permute = permutations(a,3)
print(list(permute))

#Combination
from itertools import combinations
a = [1,2,3]
combi = combinations(a,2)
    
print(list(combi))