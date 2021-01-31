# base class
class Person:
	# instance variables
	name = "Erwin Smith"
	age = 40

	# constructor
	def __init__(self):
		print("Erwin Smith was born, for the servial of humanity")

	def getODMGear(self, weight = 10):
		print("creating ODM gear with weight {}".format(weight))

if __name__ == "__main__":
	erwin = Person()
	erwin.getODMGear(weight=100)
