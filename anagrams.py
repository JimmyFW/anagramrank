import itertools
from sets import Set
import pprint
import math
from collections import OrderedDict

verbose = 0 # Toggle this to view step-by-step calculations

if verbose:
	def verboseprint(*args):
		# Print each argument separately so caller doesn't need to
		# stuff everything to be printed into a single string
		for arg in args:
			print arg,
			print
else:
	verboseprint = lambda *a:  None # This function does nothing

def sort_word(word):
	char_list = list(word) # Convert string to list of chars
	char_list.sort()
	sorted_word = ''.join(char_list) # Convert sorted list of chars to string
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
		cur_char = word[i]
		verboseprint("Looking at letter: " + cur_char)
		listlen = len(sorted_list)

		hist = histogram(sorted_list)
		histkeys = list(hist.keys())
		verboseprint("Unused characters " + str(histkeys))
		frequencies = hist.values()

		for j in range(0,histkeys.index(cur_char)):
			verboseprint("\t" + histkeys[j] + " comes before " + cur_char)
			modified_frequencies = list(frequencies)
			modified_frequencies[j] -= 1
			contribution = math.factorial(listlen-1)
			divisors = map(math.factorial, modified_frequencies)
			for divisor in divisors:
				contribution /= divisor
			verboseprint("\t" + str(listlen-1) + " / " + str(modified_frequencies))
			contributions.append(contribution)
		sorted_list.remove(cur_char)

	verboseprint(contributions)
	return sum(contributions) + 1 # add 1 since python is zero-indexed

def generate_anagrams(word):
	permlistobj = itertools.permutations(word)
	permset = Set([])

	for item in permlistobj:
		addme = ''.join(item)
		permset.add(addme)

	permlist = list(permset)
	permlist.sort()
	return permlist