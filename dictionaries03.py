name=input('Enter File Name: ')
handle=open(name)

counts=dict() #empty dictionary
for line in handle:
    words=line.split() #vamos pegar essa linha e extrair cada palavra
    for word in words:
        counts[word]=counts.get(word,0)+1 #esse aqui é o procedimento de analisar as palavras e contar elas
#print(counts)  #O output aqui dará a contagem de cada palavra

bigcount= None
bigword = None
for key,value in counts.items():
    if bigcount is None or count > bigcount:
        bigword=key
        bicount=value

print(bigword, bigcount)
