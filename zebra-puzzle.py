"""
Zebra puzzle solver:

1. There are five houses.
2. The Englishman lives in the red house.
3. The Spaniard owns the dog.
4. Coffee is drunk in the green house.
5. The Ukrainian drinks tea.
6. The green house is immediately to the right of the ivory house.
7. The Old Gold smoker owns snails.
8. Kools are smoked in the yellow house.
9. Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments.
15. The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?
"""

import itertools 

houses = range(1,6)

def is_next_to(house1, house2):
	""" Return true if house1 is next to house2, else false"""
	return abs(house1 - house2) == 1

def is_right_of(house1, house2):
	""" Return true if house1 is right of house2, else false"""
	return house1 - house2 == 1

# possible house orderings
possibilities = list(itertools.permutations(houses, len(houses)))

res = [set(), set(), set(), set(), set()]
colors = ['red', 'green', 'ivory', 'yellow', 'blue']
nationality = ['Englishman', 'Spaniard', 'Ukranian', 'Norwegian', 'Japanese']
drink = ['coffee', 'tea', 'milk', 'orange_juice', 'water']
cigs = ['Old_Gold', 'Kools', 'Lucky_Strike', 'Parliaments', 'Chesterfields']
pet = ['dog', 'snails', 'horse', 'fox', 'zebra']

def add_prop(props, vals):
	for i in range(len(props)):
		res[vals[i]-1].add(props[i])
		
def solve():
	results_gen = [ 
		add_prop([c, n, d, g, p], [eval(c), eval(n), eval(d), eval(g), eval(p)])

		for (red, green, ivory, yellow, blue) in possibilities
		if is_right_of(green, ivory) #6
		
		for (Englishman, Spaniard, Ukranian, Norwegian, Japanese) in possibilities
		if Englishman == red #2
		if Norwegian == 1 #10
		if is_next_to(Norwegian, blue)

		for (coffee, tea, milk, orange_juice, water) in possibilities
		if coffee == green #4
		if Ukranian == tea #5
		if milk == 3 #9
		
		for (Old_Gold, Kools, Lucky_Strike, Parliaments, Chesterfields) in possibilities
		if Kools == yellow #8
		if Lucky_Strike == orange_juice #13
		if Japanese == Parliaments #14
		
		for (dog, snails, horse, fox, zebra) in possibilities
		if Spaniard == dog #3
		if Old_Gold == snails #7
		if is_next_to(Chesterfields, fox) #11
		if is_next_to(Kools, horse) #12

		for c in colors 
		for n in nationality 
		for d in drink 
		for g in cigs 
		for p in pet 
	]
	return results_gen

solved = solve()
for r in res:
	print r
