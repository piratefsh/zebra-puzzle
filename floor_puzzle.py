#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def not_adjacent(f1, f2):
	return abs(f1 - f2) > 1 

def floor_puzzle():
    # Your code here

    floors = [1, 2, 3, 4, 5]

    top = floors[-1]
    bottom = floors[0]

    possible_floors = list(itertools.permutations(floors, len(floors)))
    results = ([Hopper, Kay, Liskov, Perlis, Ritchie]
	    for Hopper, Kay, Liskov, Ritchie, Perlis in possible_floors
	    if Hopper != top
	    if Kay != bottom
	    if Liskov != top and Liskov != bottom 
	    if Perlis > Kay 
	    if not_adjacent(Ritchie, Liskov)
	    if not_adjacent(Liskov, Kay)
    )

    # conditions
    return next(results)