import unittest
import anagrams

class TestRankingFunction(unittest.TestCase):

	def setUp(self):
		pass

	def test_abab(self):
		rank = anagrams.rank_anagram("abab")
		self.assertTrue(rank == 2)

	def test_aaab(self):
		rank = anagrams.rank_anagram("aaab")
		self.assertTrue(rank == 1)

	def test_baaa(self):
		rank = anagrams.rank_anagram("baaa")
		self.assertTrue(rank == 4)

	def test_question(self):
		rank = anagrams.rank_anagram("question")
		self.assertTrue(rank == 24572)

	def test_bookkeeper(self):
		rank = anagrams.rank_anagram("bookkeeper")
		self.assertTrue(rank == 10743)

	def test_nonintuitiveness(self):
		rank = anagrams.rank_anagram("nonintuitiveness")
		self.assertTrue(rank == 8222334634)

if __name__ == '__main__':
    unittest.main()