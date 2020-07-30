sh=input('Enter Hours: ')
sr=input('Enter Rate: ')
try:
    fh=float(sh) # poderia colocar int(sh) mas é melhor assim
    fr=float(sr)
except:
    print('Error, please enter a numeric input')
    quit() # não continua mais e não dará outro erro, só testar sem esse quit que verá o erro
print(fh, fr)
if fh>40:
    reg=fh*fr
    ovt=(fh-40.0)*(fr*0.5)
    pay=reg+ovt

else:
    reg=fh*fr
    pay=reg
print('Pay: ', pay)
