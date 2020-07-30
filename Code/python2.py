import random

def one(input):
    doubleS = ''
    for character in input:
        doubleS = doubleS + character + character + character
    return doubleS

def two(input):
	if (input==1):
		return False
	elif (input==2):
		return True
	else:
		for x in range(2,input):
			if(input % x==0):
				return False
	return True             

def three(a): 
	s = 0
	for i in range(1, 5):
		s += int(str(a)*i)
	return s

def four(input1, input2):
	value = ((input1 + " " + input2) * len(input1))[::len(input1) + 1]
	return str(value)

def five():
	count = 0
	nums = []
	while count < 5:
		x = random.randrange(100, 202, 2)
		nums.append(x)
		count += 1
	return nums
    
def six(input):
	lString = input.lower()
	if lString.endswith("py"):
		return True
	else:
		return False

def seven(a, b, c):
	list = [a, b, c]
	list = sorted(list)
	if (abs(list[0] - list[1])) == (abs(list[1] - list[2])):
		return True
	else:
		return False

	# <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
	
	# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

	# eight("Hello", 3) → "Ho"
	# eight("Chocolate", 3) → "Choate"
	# eight("Chocolate", 1) → "Choclate"

	# <HINT>
    # Use the cli to access the documentation help(str.replace)

def eight(input,  a):
	return ""

	# <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

	# <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

	# <HINT> 
	# There are no hints for this question.

def nine(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    if len(set1) > len(set2):
        return set2.issubset(set1)
    elif len(set2) > len(set1):
        return set1.issubset(set2)
    elif len(set2) == len(set1):
        if set(set1) == set(set2):
            return True
    else:
        return False

	# <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
	
	# The element value in the i-th row and j-th column of the array should be i*j.

	# <EXAMPLES>

	# ten(3,2) → [[0,0,0],[0,1,2]]
	# ten(2,1) → [[0,0]]
	# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

	# <HINT>
	# Think about nesting for loops.

def ten(X,Y):
	#I'll be honest, my understanding here is pretty poor, this is just butchering Stack Overflow code.
	row_num = X
	col_num = Y
	multi_list = [[1 for col in range(col_num)] for row in range(row_num)]

	for row in range(row_num):
		for col in range(col_num):
			multi_list[row][col]= row*col
	return multi_list