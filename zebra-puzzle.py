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

houses = range(5)

def is_next_to(house1, house2):
	return abs(house1 - house2) == 1

def is_right_of(house1, house2):
	return house2 - house1 == 1

# conditions

if Englishman == red #2
if Spaniard == dog #3
if codde == green #4
if Ukranian == tea #5
if is_right_of(green, ivory) #6
if Old_Gold == snails #7
if Kools == yellow #8
if milk == 2 #9
if Norwegian == 0 #10
if is_next_to(Chesterfields, fox) #11
if is_next_to(Kools, horse) #12
if Lucky_Strike == orange_juice #13
if Japanese == Parliaments #14
if is_next_to(Norwegian, blue)