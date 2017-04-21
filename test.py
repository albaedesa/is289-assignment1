
# IS 289 Week 1 Assignment Test 

from is289_assignment1 import Actor, Director
import unittest

class UnitTest(unittest.TestCase):
	
	def test_person(self):
		result = Actor("Clark", "Gable", "1901-02-01", "Gray", "Brown", "MGM").report()
		self.assertEqual(result, "Name: Clark Gable\nDOB: 1901-02-01\nEye Color: Gray\nHair Color: Brown\nStudio: MGM")
		
		result = Director("Billy", "Wilder", "1906-06-22", "27", "49").report()
		self.assertEqual(result, "Name: Billy Wilder\nDOB: 1906-06-22\nNumber of Films Directed: 27\nNumber of Awards Earned: 49")


if __name__ == "__main__":
	unittest.main()