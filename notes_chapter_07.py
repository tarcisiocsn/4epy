#THE NEW LINE CHARACTER
str='Hello\nWorld!'
print(str)
#output
#Hello
#World

str='x\ny'
print(str)
print(len(str))
#output
#x
#y
#3 - \n it's a character as x and y

#OPENING A FILE
fhand=open('mbox.txt')
print(fhand)
#output <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>
#lembrar se quiser usar um arquivo precisa está na mesma pasta aonde voce está programando
fhand=open('mbox.txt')
count=0
for line in fhand:
    count=count+1 #toda vez que encontrar uma linha adiciona ela na contagem
print('Line Count:', count)
#output Line Count: 132045

#READING THE WHOLE FILE
fhand=open('mbox-short.txt')
inp=fhand.read() #vai ler tudo, lembrar que o salto de linhas ele faz com \n e está lendo isso tbm
print(len(inp))  #saber a quantidade de characters que tem no file
#output 94626
print(inp[:20]) #do inicio até character 19, lembrar que exclui essa parte
#From stephen.marquar

#SEARCHING THROUGH A FILE
fhand=open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line) #a ideia é print todas as linhas QUE COMECEM COM FROM:
#output vai dar várias linhas espaçadas (white space) por causa do newline(\n)
#para cancelar esses white space eu uso a função rstrip() veja:

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)
#exemplo fazendo a mesma coisa
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue #skip fucntion quer dizer se uma linha não começa com From:, skip it e prin apenas o que tem
        print(line)
        #USING IN TO SELECT LINES
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line: #negocio é: se não tem esse usuario skip it e print apenas o que tem
        continue
        print(line)
