#compare list x dictionary

#list -> a linear collection of values that stay in order
#dictionary -> a 'bag' of values, each with its own label (rótulo)

#list it's similiar with pringles - very organize stuff
#dictionary - you can put every thing over there and wich part have a 'key' top open and see the value
#para simplificar é tipo tu tem uma bolsa cheia de coisa, e tu rotula as coisas com post-it tipo escreve la dinheiro no rotulo e tá la o dinheiro, escreve chave- ai ta la o postit colado na chave, ta ligado? valeu!

#dictionaries are python's most powerful data callection
#dictionaries allow us to do fast database-like operations in python
#dictionaries have different names in different languages
#associative arrays - PHP / PEARL
#properties or map or hashmap - java
#property bag - c# / .net

#dictionaries are like bags, no order

#example
purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']= 75
print(purse)
#output -> {'money': 12, 'tissues': 75, 'candy':3} #ele entrega as coisas meio sem ordem, quando eu printar pode ser diferente

print(purse['candy']) #a ideia é tipo, rotulou 3 com o nome candy, então voce pede ei me manda ai candy, ai vem o valor 3 , que tem como rotulo(label) candy
#output -> 3

purse['candy']=purse['candy']+2
print(purse)
#output -> {'money':12, 'tissues': 75, 'candy': 5} #you can see that the candy's value changed

#COMPARING LISTS AND DICTIONARIES
#Dictionaries are the lists except that they use keys instead of numbers to look up values

lst=list() #empty list and you gonna add something
lst.append(21)
lst.append(183)
print(lst)
#output ->[ 21, 183]
#detalhe que tem ordem e posição essa parada 0 e 1
#e voce n pode 'mudar' ela facilmente

ddd=dict() #dicionario vazio e vc vai acrescentar
ddd['age']=21
ddd['course']=182
print(ddd)
ddd['age']=23 #vc já quer mudar a idade ai
print(ddd)
#output -> já dará idade diferente

#DICTIONARY LITERALS
#ao inves de um empty dictionary voce usa um que voce quiser previamente
#ex:
jjj= {'chuck': 1, 'fred': 42, 'jan': 100} #isso é um dicionario
print(jjj)
#vai ser a mesma coisa que ta ai ou pode mudar de ordem, lembrar que ele n respeita a ordem
ooo={ } # isso é a mesma coisa que ooo=dict() é um dicionario vázio
print(ooo)
#output -> { }

#uma coisa interessante que dictionary faz é contar a quantidade de vezes que a palavra foi escrita
ccc=dict()
ccc['csev']=1
ccc['cwen']=1
print(ccc)
#output -> {'cserv': 1, 'cwen': 1}
ccc['cwen']=ccc['cwen']+1
print(ccc)
{'csev':1, 'cwen':2}
#output -> {'cserv': 1, 'cwen': 2}

#principio de code para histograma
counts=dict()
names=['csev', 'cwen', 'csev', 'zqian', 'cwen'] #isso é uma lista, mas posso usar para virar um dicionario
for name in names :
    if name not in counts :
        counts[name]=1 #a ideia é no dicionario aberto em cima voce acrescente 1 para cada nome que não estiver dentro do dicionario, depois disso vem o else para aumentar uma quantidade para cada nome repetido
    else: #se ele estiver no dicionario conta mais 1
        counts[name]=counts[name]+1
print(counts)
#output -> {'csev': 2, 'zquian': 1, 'cwen': 2}
if name in counts:
    x=counts[name]
else:
    x=0
x=counts.get(name,0) #esse principio é o a mesma coisa que as 4 linhas de codigo que fiz logo acima
#output -> {'csev': 2, 'zquian': 1, 'cwen': 2}

#então posso fazer a formula do histograma de tal maneira

counts=dict()
names=['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

#isso ai é bom para a gente que tá com muito index e precisa organizar o programa
#o padrão de checagem para ver se a key está no dicionario e assuma um valor se ela nào estiver lá é tão comum
#que existe um metodo chamado get() que faz isso para a gente
#coloquei get() na formula justamente para isso, coloquei um 0 quando a key ainda não foi para o dicionário, ai usa o default 0

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))
#output -> será zero, pq voce tá dizendo para acrescentar kris em um default 0
