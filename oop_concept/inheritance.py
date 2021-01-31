class GrandParent:
	def __init__(self, name):
		print("creating grand parent")
		self.name = name

class Parent(GrandParent):
	def __init__(self, grandParent):

