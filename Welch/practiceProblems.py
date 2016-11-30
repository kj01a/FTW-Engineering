def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False
		
		
def is_int(x):
	if x - int(x) == 0:
		return True
	else:
		return False

		
def digit_sum(n):
	x = 0
	for i in str(n):
		x = x + int(i)
	return x
		
x = 1234
z = 0
for i in str(x):
    z = z + int(i)
print z

import math

def factorial(x):
	return math.factorial(x)

def factorial(x):
	n = 0
	for i in str(x):
		n = n * int(i)
	return n
	
def is_prime(x):
	if x < 2:
		return False
	elif x == 2:
		return True
	else:
		for n in range(2, x-1):
			if x % n == 0:
				return False
		return True
		#You don't need an else statment in this for loop because all instances beside the conditional exceptions are true. 
		
#Got this one from the internet. I will have to come back to it later, because I was not prepared for this course to go through this bit of low level programming.
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
	
def anit_vowel(text):
	for i in text:
		if i != "a" or i != "e" or i != "i" or i != "o" or i != "u" or i != "A" or i != "E" or i != "I" or i != "O" or i != "U":
			newtext = text.replace(i, "")
	return newtext
	
def anti_vowel(text):
	x = ""
	for i in text:
		if i.lower() not in "aieou":
			x += i
	return x
	
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    x = 0
    for i in word.lower():
        if i in score:
            x += score[i]
    return x

#Censorship is wrong
def censor(text, word): 
    notarray = text.split()
    newnotarray = []
    for i in notarray:
        if i == word:
            i = "*" * len(word)
            newnotarray.append(i)
        else:
            newnotarray.append(i)
        result = " ".join(newnotarray)
    return result
	
#counting a not array
def count(sequence, item):
    x = 0
    for i in sequence:
        if i == item:
            x += 1
    return x
	
#pull out the evens
def purify(numbers):
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return evens
	
#just multipy is that so fucking hard??
def product(x):
    y = 1
    for i in x:
        y *= i
    return y
	
#easy
def remove_duplicates(numbers):
    unredundant = []
    for i in numbers:
        if i not in unredundant:
            unredundant.append(i)
    return unredundant

#find the median	
def median(numbers):
    n = sorted(numbers)
    x = len(n)
    if x % 2 == 0:
       result = (n[(x / 2) - 1] + n[x / 2]) / 2.0
    else:
        result = n[x / 2]
    return result