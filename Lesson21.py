def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DEVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(20, 5)
height = subtract(200, 25)
weight = multiply(5, 13)
iq = divide(200, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "The becomes: ", what, "Can you do it by hand?"