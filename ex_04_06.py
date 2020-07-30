def computepay(hours,rate) :
    print('In computepay', hours, rate)
    if fh>40:
        #print('Overtime')
        reg=hours*rate
        otp=(hours-40.0)*(rate*0.5)
        #print('Regular time: ', reg, 'Overtime: ', otp)
        pay=reg+otp

    else:
        #print('Regular')
        reg=hours*rate
        pay=reg
    #print('Returning',pay)
    return pay

sh=input('Enter Hours: ')
sr=input('Enter Rate: ')
fh=float(sh)
fr=float(sr)
#print(fh, fr)
xp=computepay(fh,fr) #call the function #fh será hours e fr será rate - o return pay vai retornar nesta expressão de xp
print('Pay: ', xp)
