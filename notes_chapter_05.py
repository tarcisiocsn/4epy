INTERATIONS

Repeated Steps
Program:
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!!')
print(n)

Loops (repeated steps) have iteration variables that changes each time through
a loop. Often these iteration variables go through a sequence of numbers.

A ideia desse programa é que vai acontecer o seguinte:

n é maior 0?
print(n), depois rola novamente com a definição n=n-1 logo o output fica:

OUTPUT
5
4
3
2
1
Blastoff!! pq o n ficou 0 e o while é para n>0 então pedi para print Blastoff e o novo n (print(n))
0

EXAMPLE DE INFINITE Loops
  n=5
  while n>0 # não tem nada que empeça deste loop terminar
      print('Lather')
      print('Rinse')
  print('Dry off!')

LOOP TRUE - INFINITE LOOP
while True:
    line = input('> ')
    if line=='done':
        break #para sair do loop
    print(line)
print('Done!')

Finishing an Iteration with 'Continue'
while True:
    line = input('> ')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('Done!')


DEFINITE LOOPS - easy to construct
Quite often we have a list of items of the lines in a file - effectively a finite list of things
We can write loops to run the loop once for each of the items in a set  using  the python 'for  construct
These loops are called "definite loops" because they execute an exact number of times
We say that 'definite loops iterate through the members of a set'

Example 01 - definite loop numbers
for i in [5,4,3,2,1]: # i gonna be 5,4,3,2,1 i is the iteration variable
    print(i)
print('Blastoff!')

example 02 - Definite loops with strings

friends=['Joseph', 'Glen', 'Sally']
for friend in friends: #ele ta dizendo que pegará um string na definição friends
print('Happy new year: ', friend) #não quer dizer que python sabe que friend é o singular de friends
print('Done')

OUTPUT
Happy new year: Joseph
Happy new year: Glen
Happy new year: Sally
Done

LOOPS IDIOMS: WHAT WE DO IN LOOPS
SMART LOOPS
