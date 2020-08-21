#TUPLES ARE LIKE LISTS
#A DIFERENÇA É QUE NÃO É [] E SIM ()
#position 0,1,2 etc. like a list
#TUPLES
x=('glen', 'sally', 'joseph')
print(x[2])
#output -> dará joseph
y=(1,2,9,6) #isso é um tuple
print(y)
#output -> the output is obvius

print(max(y))
#output -> 9

#so, is the samething as list

for iter in y:
    print(iter)
#output ->
#1
#2
#9
#6
#BUT....TUPLES ARE 'IMMUTABLE'
# Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
x=[9,8,7] #lembrar que isso é uma lista
x[2]=6

print(x)
# the output gonna change

y='abc'
#y[2]='d'
#se eu colocar isso dará erro, pq string é IMMUTABLE
#the samething is the tuples for example to imput those part like the example :
z=[5,4,2]
z[2]=0
#output gonna do a ERROR

#THINGS NOT TO DO WITH TUPLES
# x.sort(), x.append(), x.reverse (flip the order)
#quando voce usa um tuple é pq voce não quer modificar nada, então acaba usando TUPLES

# we can also put a tuple on the left - hand side of an assignment statement
# we can even omit the parentheses
#EXAMPLE
(x,y)=(4, 'fred')
print(y)
#output -> fred
(a,b)=(99,98)
print(a)
#output -> 99

# tuples are also related with dictionaries
# the items() method in dictionaries returns a list  of (key,values) -> TUPLES

d=dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
    print(k,v) #lembrar de sempre usar k, v para entender melhor keys and values
#output
#csev = 2
#cwen = 4

tups=d.items()
print(tups)
#output dict_items ([('csev',2)]), ([ ('cwen', 4)]) # algo como um tuple
#eu tenho 2 TUPLES

#TUPLES ARE COMPARABLE
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)
#OUTPUT -> vai dar uma parada de keys and values
