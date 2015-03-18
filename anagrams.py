import itertools
from sets import Set
import pprint
import math
from collections import OrderedDict

# ******* INSTRUCTIONS FOR VERBOSE PRINTING ****
# Toggle verbose to 1 to view step-by-step calculations
# To view just the answer, set verbose = 0
verbose = 0 

if verbose:
	def verboseprint(*args):
		# Print each argument separately so caller doesn't need to
		# stuff everything to be printed into a single string
		for arg in args:
			print arg,
			print
else:
	verboseprint = lambda *a:  None # This function does nothing

""" sort_word returns the input word sorted alphabetically
"""
def sort_word(word):
	char_list = list(word) # Convert string to list of chars
	char_list.sort()
	sorted_word = ''.join(char_list) # Convert sorted list of chars to string
	return sorted_word

""" histogram generates a histogram of letter counts.
It uses an OrderedDict and is designed to accept the output of sort_word()
"""
def histogram(L):
	d = OrderedDict.fromkeys(L)
	for key in d:
		d[key] = L.count(key)
	return d

""" print_histogram prints the histogram
"""
def print_histogram(d):
	for key in d:
		print "{} | {}".format(key, d[key])

""" rank_anagram is the special sauce.
Its workings are outlined in README.md
"""
def rank_anagram(word):
	wordlen = len(word)
	# sorted_list represents all anagram prefix groups not yet accounted for
	sorted_list = list(sort_word(word))
	# contributions represents all prefix groups accounted for, by the size of the group
	contributions = []

	for i in range(0,wordlen): # loop through each letter in the input word

		cur_char = word[i]
		verboseprint("Looking at letter: " + cur_char)
		listlen = len(sorted_list)

		# generate histogram of unaccounted prefix groups
		hist = histogram(sorted_list)
		histkeys = list(hist.keys())
		verboseprint("Unused characters " + str(histkeys))
		frequencies = hist.values()

		for j in range(0,histkeys.index(cur_char)): # loop through each letter preceding cur_char
			verboseprint("\t" + histkeys[j] + " comes before " + cur_char)

			# calculate the number of anagrams prefixed by histkeys[j]

			# histkeys[j] itself does not count in the permutations
			modified_frequencies = list(frequencies)
			modified_frequencies[j] -= 1

			# calculates number of anagrams using the multinomial function
			contribution = math.factorial(listlen-1)
			divisors = map(math.factorial, modified_frequencies)
			for divisor in divisors:
				contribution /= divisor
			verboseprint("\t" + str(listlen-1) + " / " + str(modified_frequencies))

			# append to contributions
			contributions.append(contribution)

		sorted_list.remove(cur_char) # we've added all contributions already, so remove the char

	verboseprint(contributions)
	return sum(contributions) + 1 # add 1 since python is zero-indexed

""" generate_anagrams generates a sorted list of permutations, brute-force style
It was helpful in debugging for rank_anagram
"""
def generate_anagrams(word):
	permlistobj = itertools.permutations(word)
	permset = Set([])

	for item in permlistobj:
		addme = ''.join(item)
		permset.add(addme)

	permlist = list(permset)
	permlist.sort()
	return permlist