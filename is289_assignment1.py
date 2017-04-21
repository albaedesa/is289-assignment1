
# IS 289 Week 1 Assignment 

class Person():
	
	def __init__(self, fname, lname, dob):
		self.fname = fname
		self.lname = lname
		self.dob = dob

	def report(self):
		return 'Name: {} {}\nDOB: {}'.format(self.fname, self.lname, self.dob)

class Actor(Person):

	def __init__(self, fname, lname, dob, eyeColor, hairColor, studio):
		super().__init__(fname, lname, dob)
		self.eyeColor = eyeColor
		self.hairColor = hairColor
		self.studio = studio

	def report (self):
		output = super().report()
		return output + '\nEye Color: {}\nHair Color: {}\nStudio: {}'.format(self.eyeColor, self.hairColor, self.studio)

class Director(Person):

	def __init__(self, fname, lname, dob, num_films, num_awards):
		super().__init__(fname, lname, dob)
		self.num_films = num_films
		self.num_awards = num_awards

	def report (self):
		output = super().report()
		return output + '\nNumber of Films Directed: {}\nNumber of Awards Earned: {}'.format(self.num_films, self.num_awards)

from datetime import date

clark = Actor('Clark', 'Gable', date(1901, 2, 1), 'Gray', 'Brown', 'MGM')
print(clark.report(), '\n')

billy = Director('Billy', 'Wilder', date(1906, 6, 22), '27', '49')
print(billy.report())