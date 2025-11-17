#since 28.12.2020
#
#Examples to use Tupelns in Python
#The values in a tuple are not changeable
#and the declaration happens differently, 
#otherwise they do not differ from lists or dictionaries
#Declaration:
firstTupeln = "<3",
nextTupeln = "Hello", "World", "I", "Like", "Python"

nextTupeln = nextTupeln + firstTupeln;

#Getting:
print (nextTupeln)

#Other:
#You can make a certain value in a tuple changeable by adding
#it to a list and saving the list to the tuple:
lastTupeln = "Hello", "You", "are", [15]
print (lastTupeln)
lastTupeln[3][0] = 10;
print (lastTupeln)
