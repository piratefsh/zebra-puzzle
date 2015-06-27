# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    substrs = []

    for start in range(len(text)):
        substrs.append(find_longest_from_start(text, start))
        substrs.append(find_longest_from_start(text, start+0.5))

    return max(substrs, key=lambda (x, y): y-x) if substrs else (0,0)


def find_longest_from_start(text, start):
    if isinstance(start, int):
        end = start
    else:
        start = int(start)

        if start+1 < len(text) and not equivalent(text[start], text[start+1]):
            return (start, start+1)
        end = start + 1

    while can_extend(text, start, end) and equivalent(text[start-1], text[end+1]):
        start, end = start - 1, end + 1

    return (start, end+1)


def can_extend(text, start, end):
    return start - 1 >= 0 and end+1 < len(text)

def equivalent(a, b):
    return a.lower() == b.lower()

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

def unit():
    text = 'abcde'
    assert can_extend(text, 0, 1) == False
    assert can_extend(text, 1, 1) == True
    assert can_extend(text, 1, 3) == True
    assert can_extend('abba', 1, 2) == True

    assert is_palindrome('abba') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('honey boo') == False
    assert is_palindrome('race car') == False
    assert is_palindrome('RacecarX'[0:7]) == True

    assert find_longest_from_start('racecarx', 3) == (0, 7)
    assert find_longest_from_start('abaxx', 1) == (0, 3)
    assert find_longest_from_start('xxabaxx', 1) == (1, 2)
    assert find_longest_from_start('abba', 1.5) == (0, 4)
    assert find_longest_from_start('Race carr', 7.5) == (7, 9)
    assert find_longest_from_start('Racecar', 3) == (0, 7)
    return 'tests pass'
