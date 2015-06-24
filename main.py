import itertools
import time

"""
1.  There are five houses.
2.  The Englishman lives in the red house.
3.  The Spaniard owns the dog.
4.  Coffee is drunk in the green house.
5.  The Ukrainian drinks tea.
6.  The green house is immediately to the right of the ivory house.
7.  The Old Gold smoker owns snails.
8.  Kools are smoked in the yellow house.
9.  Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments.
15. The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?
"""

def immediate_right(h1,h2):
	return h1-h2 == 1

def next_to(h1,h2):
	return abs(h1-h2) == 1

houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5] #1

house_orderings = list(itertools.permutations(houses,5))

# Englishman, Spaniard, Ukrainian, Norwegian, Japanese
# red, green, ivory, yellow, blue
# Coffee, tea, Milk, oj, water
# dog, snails, fox, horse, zebra
# OldGold, Kools, Chesterfields, LuckyStrike, Parliaments 
g = ((zebra, water)
	for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in house_orderings
	for (red, green, ivory, yellow, blue) in house_orderings
	for (Coffee, tea, Milk, oj, water) in house_orderings
	for (dog, snails, fox, horse, zebra) in house_orderings
	for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in house_orderings
	if Englishman == red 	#2
	if Spaniard == dog 		#3
	if Coffee == green		#4
	if Ukrainian == tea		#5
	if immediate_right(green, ivory) #6
	if OldGold == snails	#7
	if Kools == yellow		#8
	if Milk == middle		#9
	if Norwegian == first	#10
	if next_to(Chesterfields,fox) #11
	if next_to(Kools,horse)	#12
	if LuckyStrike == oj	#13
	if Japanese == Parliaments #14
	if Norwegian == blue	#15
	)

start = time.time()
print next(g)
end = time.time()
print 'Time:', end - start