string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	word_count = { }
	words = string1.split()
	for word in words:
		word_count[word] = word_count.get(word, 0) +1
	print word_count
	return word_count

# count_unique(string1 + " " + string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    new_list = []
    for num in list1:
    	for i in list2:
    		print "0.0  i = " + str(i) + "  " + "num = " + str(num)
    		if num == i:
    			print "0.1  i = " + str(i) + "  " + "num = " + str(num)
    			new_list = new_list + [num]
    			print "0.2 new list",
    			print new_list
    			
    print new_list
    return new_list

common_items(list1, list2)

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    new_list = {}
    for num in list1:
    	for i in list2:
    		print "0.0  i = " + str(i) + "  " + "num = " + str(num)
    		if num == i:
    			print "0.1  i = " + str(i) + "  " + "num = " + str(num)
    			new_list[num] = new_list.get(num, 0) + 1
    			print "0.2 new list",
    			print new_list
    print new_list
    return new_list

common_items2(list1, list2)
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):



    pass

list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
sum_zero(list1)
sum_zero(list2)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    pass

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
