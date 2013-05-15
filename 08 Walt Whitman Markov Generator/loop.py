for key, thelist in dictionary.items():
	for index in thelist:
		print "%s has item %s" % (key, index)


import random

for key, thelist in dictionary.items(): # for a dictionary where the value is a list
	#length = len(value) # how long the value list is - UNNECESSARY
	#a = range(0,length) # returns a list "a" from 0 to length - UNNECESSARY
	b = random.randint(0,len(thelist))
	print "A random value in %s is %s" % (key, thelist[b])