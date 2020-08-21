#Counting Pattern
#the general pattern to count the words in a line of the text is to split the line
#into words, then loop through the words and use a dictionary to track the count of
#each word independently

counts=dict()
print('Enter a line of text: ')
line=input('') #se não colocar a definição de line essa porra dá erro quando for printar
words=line.split()  # quer dizer que o texto que foi colocado virá a tona ;)
print('Words: ', words)

print('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1 #isso significa que voce add um novo elemento por isso o 0 ou add um já existente e soma 1 nele - ou seja, no texto terá palavras repetidas e outras que não são repetidas e essa formula se encaixa bem nessa opção
print('Counts',counts) #lembrar que na linha 13 eu to criando um dicionário no loop

#Definite Loops Dictionaries
counts={'fred':42, 'chuck':1, 'jan':100} # this is a dictionary
for key in counts:
    print(key, counts[key])
#Even through dictionaries are not stored in order, we can write a 'for' loop that goes
#through all the entries in a dictionary - actually it goes through all of the keys in the
#dictionary and looks up the values.

#output ->
#jan 100
#chuck 1
#fred 42 lembrar que aqui a ordem nÃo importa

jjj={ 'chuck':1, 'fred':42, 'jan':100}
print(list(jjj))
#output -> [ 'jan', 'chuck', 'fred']
print(jjj.keys()) #aqui só printa os keys do dicionario
print(jjj.values()) #aqui só print the values of the dictionary
print(jjj.items()) #[{('jan:100), ('chuck':1 ), ( 'fred':42)}]

# se vc perceber voce faz uma lista com cada item - keys, values e both que é items

#BONUS : TWO ITERATION VALUES
jjj=jjj
for aaa,bbb in jjj items():
    print(aaa,bbb)
#jan 100
#chuck 1
#fred 42

# aaa=keys and bbb=values
