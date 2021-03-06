# ----------------
# User Instructions
#
# Modify the timedcalls(n, fn, *args) function so that it calls 
# fn(*args) repeatedly. It should call fn n times if n is an integer
# and up to n seconds if n is a floating point number.

import itertools

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def test_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((Englishman, green)
                for (red, green, ivory, yellow, blue) in c(orderings)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                if Englishman is green and red is 2
                # red = 1, green = 2, ... calls = 1, items = 1  
                # Eng = 1, Span = 2, ...  calls = 2, items = 2
                # Eng = 1, Span = 2, ...  calls = 2, items = 3
                # ...
                # Eng = 5, 4, 3, 2, 1 ...  calls = 2, items = 121
                # red = 2, green .... calls = 2
                # Eng  .. calls = 3
                
                )


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""

    times = []
    
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    
    elif isinstance(n, float):
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    else:
        raise ValueError("Argument n should be either int or float type: %s" % str(n))    
    return min(times), average(times), max(times)

def c(sequence):
    c.calls += 1 
    for item in sequence:
        c.items += 1
        yield item 

def instrument_fn(fn, *args):
    c.calls, c.items = 0, 0
    result = fn(*args)
    print '%s got %s with %5d iterations over %7d items' % (fn.__name__, result, c.calls, c.items)


