class MyStuff(object):
	"""docstring for MyStuff"""

	def __init__(self, arg):
		self.tangerine = "And now a thousand years between %s" % arg
	def apple(self):
		print "I AM CLASSY APPLES."
		
thing = MyStuff("you and me.")
thing.apple()
print thing.tangerine