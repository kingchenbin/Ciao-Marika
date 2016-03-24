# You know that I am actually an experienced programmer.
# But I am kind of OCD or something.

from sys import argv

script, user = argv

print "Hello %s, let's begin." % user
print "You've already got 'from' and 'import'."

if 2 < 3 and not 9.7 == 5:
	print "And this is for 'and' and 'not'."

list = ["Alvin", "Being", 4, "Simon", "Theodore", 0]
for item in list:
	print "%r" % item
print "We now have 'for', 'in' and 'print'."

del list[1:3] # remove element #1 and #2
for item in list:
	if 'Alvin' == item:
		continue
	print "%r" % item
print "See the difference? That is 'del' and 'continue'."

idx = 2
while idx > 0 or False:
	if idx > 2:
		pass
	elif idx == 2:
		print "This is for 'or', 'while' and 'elif'"
	else:
		print "This is for 'pass', 'if' and 'else'"
		break
	idx -= 1

if idx == 1:
	print "And 'break' works fine!"

def func_whatever():
	print "We are in something called 'def' and 'return'."
	return "If you are in danger, CALL 911!!!"

A_COMPLICATED_LIST_INVOVING_A_LOT_OF_TYPES_AND_VALUES_ACTUALLY_I_AM_JUST_BLUFFING = \
[1, ['Aria', 3.1415926], "CHIPS", False, 9999999999, [[1.3055]]]

print A_COMPLICATED_LIST_INVOVING_A_LOT_OF_TYPES_AND_VALUES_ACTUALLY_I_AM_JUST_BLUFFING

