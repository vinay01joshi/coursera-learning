x = ['Now', 'we', 'are', 'cooking']
print(type(x))

print(len(x))
print('are' in x)
print(x[0])
print(x[1:3])


def group_list(group, users):
  members = '{}: {}'.format(group, ', '.join(users))
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"


fruites = ['Pineapple', 'Banana' ,'Orange', 'Apple','Kiwi']
fruites.append('Grapes')
fruites.insert(0,'Malon')
fruites.remove('Malon') # removing the element
fruites.pop(3) # removing method from index
fruites[2] = "Malon"
print(fruites);


def skip_elements(elements):
	# code goes here
	list_length = len(elements)
	new_list = []
	for x in range(0,list_length,2):
	  new_list.append(elements[x])
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# Tuples

fullname =['vinay','joshi']

def guest_list(guests):
	for tuples in guests:
	  name,year,work = tuples
	  print('{} is {} years old and works as {}'.format(name,year,work))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

winners = ['Vinay','Joshi','Tanuja','Dhyani']
for index, person in enumerate(winners):
    print("{} - {}".format(index,person))

def skip_elements(elements):
	# code goes here
	new_list = []
	for index, chars in enumerate(elements):
	  if index % 2 == 0 :
	    new_list.append(chars)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


def full_emails(people):
    result = []
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_emails([("vinay01joshi@gmail.com","Vinay Joshi"),("tanuja01dhyani@gmail.com","Tanuja Dhyani")]))

# List comphrehencive

multiples = [ x *7 for x in range(1,11)]
print(multiples)

programming_languages = ['Python','Java','c','c++','C#','Javascript','ruby']
lenght_list = [ len(x) for x in programming_languages ]
print(lenght_list)

z = [ x for x in range(1,101) if x % 3 == 0 ]
print(z)


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [(x,x[:x.index('.')+2]) for x in filenames]
print(newfilenames)