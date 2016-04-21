class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
	def override(self):
		print "PARENT override()"
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

class Other(object):
	def override(self):
		print "Other override()"
	def implicit(self):
		print "Other implicit()"
	def altered(self):
		print "Other altered()"

class Child1(object):
	def __init__(self):
		self.other = Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		self.other.altered()
		print "CHILD, AFTER PARENT altered()"

son = Child()

son.implicit()
son.override()
son.altered()