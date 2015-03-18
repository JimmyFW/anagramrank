import itertools
from sets import Set
import pprint
import math
from collections import OrderedDict

def sort_word(word):
	char_list = list(word) # convert string to list of chars
	char_list.sort()
	sorted_word = ''.join(char_list) # convert sorted list of chars to string
	return sorted_word

def histogram(L):
	d = OrderedDict.fromkeys(L)
	for key in d:
		d[key] = L.count(key)
	return d

def print_histogram(d):
	for key in d:
		print "{} | {}".format(key, d[key])

def rank_anagram(word):
	wordlen = len(word)
	sorted_list = list(sort_word(word))
	contributions = []
	for i in range(0,wordlen):
		cur_char = word[i] # first letter is M
		print "Looking at letter: " + cur_char
		listlen = len(sorted_list)

		# which letters in the histogram come before M?
		hist = histogram(sorted_list)
		histkeys = list(hist.keys())
		print "Unused characters " + str(histkeys)
		frequencies = hist.values()

		for j in range(0,histkeys.index(cur_char)):
			print "\t" + histkeys[j] + " comes before " + cur_char
			modified_frequencies = list(frequencies)
			modified_frequencies[j] -= 1
			contribution = math.factorial(listlen-1)
			divisors = map(math.factorial, modified_frequencies)
			for divisor in divisors:
				contribution /= divisor
			print "\t" + str(listlen-1) + " / " + str(modified_frequencies)
			contributions.append(contribution)
		sorted_list.remove(cur_char)

	print contributions
	return sum(contributions) + 1

def generate_anagrams(word):
	permlistobj = itertools.permutations(word)
	permset = Set([])

	for item in permlistobj:
		addme = ''.join(item)
		permset.add(addme)

	permlist = list(permset)
	permlist.sort() # update sort function to be more domain specific
	return permlist