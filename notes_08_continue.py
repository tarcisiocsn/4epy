#best friends : Strings and Lists
abc='With three words'
stuff=abc.split()
print(stuff)
#output-> ['With', 'three', 'words'] , so this will be a list

print(len(stuff))
#output -> 3
print(stuff[0])
#output ->with
for w in stuff:
    print(w)
#output ->
#with
#three
#words

line='a lot of                 space' # example of split() running with a lot of space between the words
etc=line.split()
print(etc)
#output -> ['a', 'lot', 'of', 'space']

#At the mbox-short we have a lot of mails, and days...like :
#From stephen.marquard@uct.ac.za 'Sat' Jan 5 09:14:16 2008
#so I need to extract the days on mail, so I gonna show it now:

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    print(words[2]) #ai vai mostrar os dias que estão no email lá ! #tem que se ligar que nos emails, o dia está na segunda posição from é a posição 0
#really nice!

line='From stephen.marquard@uct.ac.za Jan 5 09:14:16 2008'
words=line.split()
print(words)
#so now, wich words will be in a list! stephen.marque... is only one word

#extract the domain at the email address ex. uct.ac.za

#primeiro transformar line em lista usando spli()
words=line.split()
email=worlds[1] #pq o email será a posiçÃo numero 1 -> stephen.marquard@uct.ac.za
pieces=email.split('@') #então vai virar uma lista separando o que tem antes do @ e o deppois
#output -> [ ' stephen.marquard', 'uct.ac.za']
print(pieces[1]) #o output será justamente uct.ac.za

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
#output -> lar@freecodecamp.org 
