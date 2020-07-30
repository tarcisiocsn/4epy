str = 'X-DSPAM-Confidence: 0.8475'
print(str)
pos1=str.find(':')
print(pos1)
#output 18
pos2=str.find('5',pos1) #procurar o 5 a partir de pos1
print(pos2)
#output 25
num=str[pos1+1:pos2+1]
print(num)
#output 0.8475
print(type(num))
#output 'str'
#A questão pede para ele virar um float number
fx=float(num)
print(type(fx))
print(num)
