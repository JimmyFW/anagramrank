import sys
import anagrams
import pprint
from anagrams import rank_anagram

if __name__ == '__main__':

	try:
		word = sys.argv[1]
	except IndexError:
		print "Not enough arguments"
		raise

	# takes a word, sorts its characters a-z, prints a histogram of the characters

	if len(sys.argv) == 3 and sys.argv[2] == '--help':
		print "Options are: --sort and --brute50"

		print "--sort takes a word, sorts its characters a-z"
		print "and prints a histogram of the characters"

		print "--brute50 takes a word, generates all anagrams"
		print "and prints the first 50"

	elif len(sys.argv) == 3 and sys.argv[2] == '--sort':
		sorted_word = anagrams.sort_word(word)
		hist = anagrams.histogram(sorted_word)
		print sorted_word
		anagrams.print_histogram(hist)

	elif len(sys.argv) == 3 and sys.argv[2] == '--brute50':
		permlist = anagrams.generate_anagrams(word)
		pprint.pprint(permlist[:50])
		print permlist.index(word) + 1

	else: # default behavior is to find the rank
		rank = rank_anagram(word)
		print rank