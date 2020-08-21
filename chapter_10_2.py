fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
#print('Counts: ' , counts) #aparecerá a quantidade de vezes que cada palavra apareceu no texto

lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted(lst, reverse=True) #ordena a lista

# de lst até a parte do sorted eu posso fazer apenas em uma linha - ver exemplo abaixo depois da função printa
for val,key in lst[:10]:
    print(key,val)

#exemplo

c = {'a':10, 'b': 1, 'c': 22}

#quero ordenar a lista
print( sorted( [ (v,k) for k,v in c.items() ] ) )
#output -> [(1, 'b'), (10, 'a'), (22, 'c')]
