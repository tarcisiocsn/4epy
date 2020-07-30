sh=input('Enter Hours: ')
sr=input('Enter Rate: ')
fh=float(sh) # poderia colocar int(sh) mas é melhor assim
fr=float(sr)
#print(fh, fr)
if fh>40:
    print('Overtime')
    reg=fh*fr
    ovt=(fh-40.0)*(fr*0.5) #isso é o valor da hora extra -> 50% do valor de rate
    print('Regular time: ', reg, 'Overtime: ', ovt)
    pay=reg+ovt # lá no final ele vai printar o pay deste caso

else:
    print('Regular')
    reg=fh*fr
    pay=reg
print('Pay: ', pay)
