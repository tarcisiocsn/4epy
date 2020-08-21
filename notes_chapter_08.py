#LIST A
#   what is not a 'collection'
#   Most of our variables have one value in them -when we put a new value in the variable, the old value is overwritten
# ex -
# x=2
#x=4
#print(x)
#output - 4

#A LIST IS A KIND COLLECTION
# A collection allows us to put many values in a single 'variable'
# a collection is nice because we can carry all many values around in one convenient package

#ex: friends = [ 'joseph', 'Glen', 'sally']
#ex: carryon - [ 'socks', 'shirt', 'perfume']

#LIST CONSTANTS
# list constants are surrounded by square brackets and the elements in the list are separated by commas

#A list element can be any python object - even another list print(['apple', [ 5,6], 7, 8, 'red'])

#a list can be empty ex: print([])

for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

#Lists and definite loops - best pals
friends=['joseph', 'glen', 'sally']
for friend in friends: #lembrar que não tem nada a ver singular e plurar nesse caso poderia ser x e y
    print('Happy new year: ',friend)
print('Done')

#poderia usar no exemplo assima x=[.....] e for y in x print('Happy new year: ', y)

#LIST HAS POSITION

#Just like strings, we can get at  any single element in a list using an index specified in square brackets
#ex: friends=['x', 'y', 'z'] #it starts by 0 and go!
#print(friends[1])
#output -> y

#LIST A MUTABLE
#Strings are 'immutable' -we cannot change the contents of a string - we must make a new string to make any change
# List are 'mutable' - we can change an element of a list using index operator

#example
lotto=[5,20,35,40]
lotto[1]=100
print(lotto)
#output - [5,100,35,40]

#HOW LONG IS A LIST
#WE USE len() function
#example
#x=[5,'joe',35,40]
#print(len(x))
#output -> 4 #we have 4 position

#A TALE OF TWO LOOPS
friends=['joseph', 'glen', 'sally']
#for friend in friends:
    #print('Happy new year: ', friend)

for i in range(len(friends)):
    friend=friends[i]
    print('Happy new year: ', friend)
#range(len(friends)) - gives me [0,1,2] - pq range e len combinados dará as posições do início dessa lista até o final
#melhor usar a primeira véi! mais fácil essa buceta

#CONCATENATING LISTS USING +

#we can create a new list by adding two existing lists together
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

#LIST CAN BE SLICED USING :
#example
t=[9,30,45,60,89,90]
print(t[1:3])
#output-> [30,45] lembrar que o 3 não entra
#os demais pode ser usado tipo
#t[:4] vai até a posição 3
#t[4:] vai da posição 4 até final
#t[:] pega todos

#from scratch - do princípio

#BUILDING A LIST FROM SCRATCH
# we can create an empty list and then add elements using 'append' method
#example
stuff=list()
stuff.append('book')
stuff.append(99)
print(stuff)
#output -> ['book', 99]

#the list stay in order and new elements are added at the end of the list
#example
#stuff.append('cookie')
#print(stuff)
#output-> ['book', 99, 'cookie']

#IS SOMETHING IN A LIST?
# IN AND NOT IN - MUITO USADO PARA LOOP
#some=[10,9,5,16]
#9 in some - is 9 in some?
#true
#15 in some
#false
#20 not in some
#true

#SORT A LIST

#friends=['joseph','glen', 'sally']
#friends.sort()
#print(friends) - dará uma sortida na lista

#BUILT-IN FUNCTIONS AND LISTS

num=[3,41,12,9,74,15]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num)) #average

total=0
count=0
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    value=float(inp)
    total=total+value
    count=count+1
average=total/count
print('average: ', average)

#using list

numlist=list() #this is an empty LIST
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    value=float(inp)
    numlist.append(value) #cada vez que colocar um número vai entrando na lista, basicamente essa função
average=sum(numlist)/len(numlist)
print('Average: ', average)
