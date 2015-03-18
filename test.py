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

	def test_dddddddddddddddddddd(self):
		rank = anagrams.rank_anagram("dddddddddddddddddddd")
		self.assertTrue(rank == 1)

	def test_twentysix(self):
		rank = anagrams.rank_anagram("twentysix")
		self.assertTrue(rank == 106029)

	def test_twentysixl(self):
		rank = anagrams.rank_anagram("twentysixl")
		self.assertTrue(rank == 1151030)

	def test_twentysixle(self):
		rank = anagrams.rank_anagram("twentysixle")
		self.assertTrue(rank == 6731964)

	def test_dddddddddda(self):
		rank = anagrams.rank_anagram("dddddddddda")
		self.assertTrue(rank == 11)

	def test_none(self):
		rank = anagrams.rank_anagram("")
		self.assertTrue(rank == 1)

if __name__ == '__main__':
    unittest.main()