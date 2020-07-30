#STRINGS
#looking inside strings
#começa por 0 todas as letras da strings
#Posição do caracter número 2 da palavra banana
fruit='banana'
letter=fruit[1]
print(letter)
#OUTPUT - a

x=3
w=fruit[x-1]
print(w)
#OUTPUT n

#STRINGS HAVE LENGHT
#ou seja quantas letras a string tem
fruit='banana'
print(len(fruit))
#OUTPUT - 6
#len is a function buit-in

#LOOPING THROUGH strings
fruit='banana'
index=0
while index < len(fruit): #quando voce coloca len vira um número, então será de 0 até 5, pq mesmo sendo 6 letras, voce tem que imaginar que irá do 0 a 5, além que ele ele fala que é menor e não menor igual
    letter = fruit[index] #esse aqui vai mostrar a posição da letra fruit[0] - será b E AI POR DIANTE
    print(index,letter)
    index=index+1 #Parametro para ter a contagem
#OUTPUT
#0 b
#1 a
#2 n
#3 a
#4 n
#5 a

#LOOPING THROUGH STRINGS
fruit='banana'
for letter in fruit:
    print(letter)
#output
# b
# a
# n
# a
# n
# a

#A definite loop using a 'for' statement is much more elegant

#LOOPING AND COUNTING
word='banana'
count=0
for letter in word:
    if letter == 'a': #para saber quantos 'a' tem na palavra
        count=count+1
print(count)

#SLICING STRINGS
s='Monty Python'
print(s[0:4]) #ele quer imprimir do caracter 0 para 4, mas lembrar que não conta o 4 e sim o 3
#output Mont
print(s[6:7])
#output P - pq o espaço conta como um caracter
print(s[6:20])
#output Python , mesmo não indo até 20

print(s[:2]) #do 0 até 1
#output Mo
print(s[8:]) #do 8 até o final
#output thon
print(s[:]) #não sei para que essa merda
# output Monty Python

#STRING CONCATINATION
a='hello'
b=a+'there'
print(b)
#output hellothere #nÃo tem espaço automatico como print('hello',there)

c=a+' '+'there' #tem que dar um espaço entre os ''
print(c)
#output hello there

#STRING LIBRARY - FUNCTIONS
greet='Hello Bob'
zap=greet.lower() #se colocar .upper() fica tudo maiuscula
print(zap)
#output - hello bob - tudo minusculo
print('HI There'.lower())
#output - hi there
#tem várias funções para str. então é pesquisar na internet e ver se encaixa

fruit='banana'
pos=fruit.find('na')
print(pos)
#output - 2
aa=fruit.find('z')
print(aa)
#output - -1 pq não tem na parada

#REPLACE
greet='Hello Bob'
nstr=greet.replace('Bob', 'Jane')
print(nstr)
#output - Hello Jane
nstr=greet.replace('o','x')
print(nstr)
#output - Hellx Bxb

#STRIPPING WHITESPACE
greet=' hello there '
greet=greet.lstrip()
print(greet)
#output - 'hello there '
greet=' hello there '
greet=greet.rstrip()
print(greet)
#output - ' hello there'
greet=' hello there '
greet=greet.strip()
print(greet)
#output - 'hello there'

#PARSING AND STRACTING
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
#output  21
sppos=data.find(' ', atpos) # seria procurar em que posição está o espaço a partir de atpos
print(sppos) #lembrar que coloquei entre pareteses e virgula então ele incluirá atpos
#output 31
host=data[atpos+1:sppos] #ele não incluirá sppos
print(host)
#output .uct.ac.za 
