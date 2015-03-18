# anagramrank

Instructions
=====

Included in this submission are three files: anagrams.py, cli.py, and test.py.

## anagrams.py
anagrams.py is a collection of functions, including anagram_rank(word), which is an algorithm which computes the index of a word within the alphabetically sorted list of all of that word's anagrams.

NOTE: To see a printout of all of the steps used in calculating the result, simply go into anagrams.py, and set

    verbose = 1

Otherwise leave it as 0.

## cli.py
cli.py is a command line interface. Its usage is as follows:

    > python cli.py bookkeeper
    10743
    
You can also time the calculation.

    > python cli.py bookkeeperhelloworld --time
    6349469353074
    1 milliseconds elapsed.

It also comes with the option to attempt to brute force the problem by generating the whole list, sorting that list, and searching for the word within the list. it will print the first 50 elements of that list, and then print the index.

    > python cli.py bookkeeper --brute50
    ['beeekkoopr',
     'beeekkoorp',
     'beeekkopor',
     'beeekkopro',
     .
     .
     .
     'beeekprook',
     'beeekrkoop',
     'beeekrkopo']
    10743

## test.py
test.py is essentially a unit test suite. I used all of the given examples in this test suite, as well as some results that I brute force computed.

The tests include: empty string, a string of 20 d's, and the string "twentysixle".

    > python test.py
    ............
    ----------------------------------------------------------------------
    Ran 12 tests in 0.005s
    OK

Note 1: I didn't have a way to brute force the solution for strings of 20 letters, but an answer is given well under 500 milliseconds (more like 1 or 2 milliseconds)

Note 2: It turns out that python automatically switches between 32-bit integers and bignums, so the program can handle 20 letter input words with no problem.

The Algorithm
=====
The algorithm relies on four data structures:

1. sorted_list, which is a list of the input word letters sorted alphabetically. Letters are popped off from the front of sorted_list as the algorithm accounts for the number of anagrams contributed by these letters.
2. histkeys, which is a list of the input word letters without duplicates, sorted alphabetically
3. frequencies, which is a list of counts of letter occurrence in the input word, where the count index matches with the letter's index in histkeys
4. contributions, which is a list of ints which, when summed, give the anagram rank of the input word

The algorithm essentially counts the number of anagrams which preceeds the input word in the alphabetically sorted anagram list. The multinomial formula allows us to count the permutations of a set of letters with repeating elements.

For example, if we're looking at the input word QUESTION, we know that a bunch of anagrams precede it in the anagram list. Several of these anagrams are prefixed with QUEI. The remaining letters available for permutation are S, T, O, and N. There are 4! ways to permute these letters. Therefore, the "contribution" of this group of anagrams is 4!.

See the "Notebook" section below to see the full calculation trace for the input word QUESTION.

Thought Process
=====


First I thought about the feasibility of a brute force solution. 20 letter words will generate a max of 20! different anagrams. The constraints given (half a second response time) made this approach look grim.

Next I decided to check out the solution space interactively. I made a CLI where, if you gave it a word with no arguments, it would simply spit out all anagrams of that word in order.

The ordered list reminded me of counting problems we were given in MTH2110 Discrete Math. If I could partition the ordered list in the right way, I would be able to count the number of elements which occurred before the search element. That would give me the index.

Notebook
=====

Here are some of my notes as I was manually running through test cases (using the given sample words):

### QUESTION
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



### QUESTIONQ
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


### MISSISSIPPI
IIIIMPPSSSS

First letter is M. I comes before M.
    How many anagrams start with I? 10!/4!/2!/3!
Second letter is I. None
Third letter is S. I,P come before S in the sorted list
    How many anagrams start with MII? 8!/2!/2!/4!
    How many anagrams start with MIP? 8!/3!/1!/4!
