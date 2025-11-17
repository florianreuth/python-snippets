#since 28.12.2020
#
#To Save: [Title, Author, BookNumber, Price]
# First Programm (with List)
books = [["Python 3", "Michael Bonacina", "1337", "10 Pounds"],
         ["Java", "Paul Fuchs", "1338", "12 Pounds"],
         ["HTML5 & CSS3", "Paul Fuchs", "1339", "14 Pounds"]]
print ("Found 3 Books")
print ("Name", books[0][0])
print ("Author", books[0][1])
print ("Book Number", books[0][2])
print ("Price", books[0][3], "\n")

print ("Name", books[1][0])
print ("Author", books[1][1])
print ("Book Number", books[1][2])
print ("Price", books[1][3], "\n")

print ("Name", books[2][0])
print ("Author", books[2][1])
print ("Book Number", books[2][2])
print ("Price", books[2][3], "\n")

# Next Programm (with Dictionary)
nextBooks = [{"Name": "Python", "Author": "Michael Bonacina", "BookNumber": "1337", "Price": "10 Pounds"},
             {"Name": "Java", "Author": "Paul Fuchs", "BookNumber": "1338", "Price": "12 Pounds"},
             {"Name": "HTML5 & CSS3", "Author": "Paul Fuchs", "BookNumber": "1339", "Price": "14 Pounds"}]
print ("Found 3 Books")
print ("Name", nextBooks[0]["Name"])
print ("Author", nextBooks[0]["Author"])
print ("Book Number", nextBooks[0]["BookNumber"])
print ("Price", nextBooks[0]["Price"], "\n")

print ("Name", nextBooks[1]["Name"])
print ("Author", nextBooks[1]["Author"])
print ("Book Number", nextBooks[1]["BookNumber"])
print ("Price", nextBooks[1]["Price"], "\n")

print ("Name", nextBooks[2]["Name"])
print ("Author", nextBooks[2]["Author"])
print ("Book Number", nextBooks[2]["BookNumber"])
print ("Price", nextBooks[2]["Price"], "\n")

#Last Programm (with Tubeln)
lastBooksFirst = "Python", "Michael Bonacina", "1337", "10 Pounds"
lastBooksNext = "Java", "Paul Fuchs", "1338", "12 Pounds"
lastBooksLast = "HTML5 & CSS3", "Paul Fuchs", "1339", "14 Pounds"
print ("Found 3 Books")
print ("Name", lastBooksFirst[0])
print ("Author", lastBooksFirst[1])
print ("Book Number", lastBooksFirst[2])
print ("Price", lastBooksFirst[3], "\n")

print ("Name", lastBooksNext[0])
print ("Author", lastBooksNext[1])
print ("Book Number", lastBooksNext[2])
print ("Price", lastBooksNext[3], "\n")

print ("Name", lastBooksLast[0])
print ("Author", lastBooksLast[1])
print ("Book Number", lastBooksLast[2])
print ("Price", lastBooksLast[3], "\n")
