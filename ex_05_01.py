num=0
tot=0.0
while True :
    sval=input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input')
        continue #isso é que depois do error ele pode continuar no loop
    #print(fval)
    num=num+1
    tot=tot+fval
#print('ALL DONE')
print(tot, num, tot/num)
#se não entender o num - ele tá ai para ser uma variavel de contagem de quantos input voce colocou ver loop.py
