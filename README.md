# anagramrank

Thought Process
=====


First I thought about the feasibility of a brute force solution. 20 letter words will generate a max of 20! different anagrams, which is way bigger than sys.maxint. The constraints given (half a second response time) made this approach look grim.

Next I decided to check out the solution space interactively. I made a CLI where, if you gave it a word with no arguments, it would simply spit out all anagrams of that word in order.

The ordered list reminded me of counting problems we were given in MTH2110 Discrete Math. If I could partition the ordered list in the right way, I would be able to count the number of elements which occurred before the search element. That would give me the index.

Notebook
=====

Here are some of my notes as I was manually running through test cases (using the given sample words):
ABAB
=====
4 elements, 2 groups
4!/2!/2! = 6 anagrams total
AABB (sorted)

How many anagrams start with ...
AA? 1
ABAB? 1

total = 2

diff approach ...
first letter of word is A
	place of A is 0 in AABB
		so we move on
second letter of word is B
	place of B is 1 in ABB
		so we account for the case AA, and it turns out there is only one anagram which starts with AA
		this is true because we run the hypothetical:
			assuming we've used up the letters AA, how many ways are there to arrange the remaining letters?
third letter of word is A
	place of A is 0 in AB
		so we move on
fourth letter of word is B
	place of B is 0 in B
		so we move on
done


QUESTION
=====
8 elements, each unique
8! anagrams total

EINOQSTU (sorted)

How many anagrams start with ...

E? 7!
I? 7!
N? 7!
O? 7!

QE? 6!
QI? 6!
QN? 6!
QO? 6!
QS? 6!
QT? 6!

QUEI? 4!
QUEN? 4!
QUEO? 4!

QUESI? 3!
QUESN? 3!
QUESO? 3!

QUESTIN? 2!

QUESTION? 1

total = 24572



QUESTIONQ
=====
9 elements
9!/2! anagrams total

EINOQQSTU (sorted)

How many anagrams start with ...

E? 8!/2!
I? 8!/2!
N? 8!/2!
O? 8!/2!

QE? 7!
QI? 7!
QN? 7!
QO? 7!
QQ? 7!
QS? 7!
QT? 7!


MISSISSIPPI
=====
IIIIMPPSSSS

First letter is M. I comes before M.
	How many anagrams start with I? 10!/4!/2!/3!
Second letter is I. None
Third letter is S. I,P come before S in the sorted list
	How many anagrams start with MII? 
	How many anagrams start with MIP?

Initial approach
=====

First I solved the problem of ranking only words with no repeating characters.

		#place = sorted_list.index(cur_char)
		#contributions.append(math.factorial(len(sorted_list)-1)*place)