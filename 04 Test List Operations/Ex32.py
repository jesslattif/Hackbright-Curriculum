the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

#mixed lists; have to use %r since don't know what's in it
for i in change:
	print "I got %r" % i

#can also build lists; start w/an empty one
elements = []

# use the "range" function to do 0 - 5 counts
for places in range(0, 6):
	print "Adding %d to the list." % places
	#append is a function that lists understand
	elements.append(places)



#now print them
for places in elements:
	print "Element was: %d ." % places
