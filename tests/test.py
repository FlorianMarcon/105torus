import unittest

class Test(unittest.TestCase):
	def first(self):
		self.assertEqual('foo'.upper(), 'FOO')

if __name__== '__main__':
	unittest.main()
