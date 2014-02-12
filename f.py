def double(x):
	return 2 * x

def triple(x):
	return 3 * x

def add1(x):
	return x + 1

numbers = [2,3,4,5,6]
all_doubles=[]
for n in numbers:
	all_doubles.append(double(n))
print all_doubles

all_larger=[]
for n in numbers:
	all_larger.append(add1(n))
print all_larger

def call_something(the_function, the_value):
	return the_function(the_value)

call_something(triple, 9)


def for_each(function, values):
	result=[]
	for v in values:
		tmp = function(v)
		result.append(tmp)
	return result

print for_each(triple, [1,2,3])

def zipper(function, left, right):
	result=[]
	for i in range(len(left)):
		tmp = function(left[i], right[i])
		result.append(tmp)
	return result

def add_up(a,b):
	return a+b

def square(x):
	return x*x

print zipper(add_up, [1,2,3],[4,5,6])
print zipper(max, [3,5,1],[2,7,9])

print for_each(square, zipper(max,[1,10],[2,3]))
