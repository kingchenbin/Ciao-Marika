class MyStuff(object):
	"""docstring for MyStuff"""

	def __init__(self, arg):
		self.tangerine = "And now a thousand years between %s" % arg
	def apple(self):
		print "I AM CLASSY APPLES."
		
thing = MyStuff("you and me.")
thing.apple()
print thing.tangerine

class Song(object):
	"""docstring for Song"""
	def __init__(self, arg):
		self.lyrics = arg

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right here"])

bulls_on_parade = Song(["They really around the family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
