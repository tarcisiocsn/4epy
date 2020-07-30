def greet(lang): #greet is saudações #lang é tipo language
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
#A parameter is a variable which we use in the function
#It's a "hangle" that allows the code in the function to
#access the arguments for a particular function invocation
greet('es')
greet('fr')
greet('en')

# Return Values
def greet(lang): #greet is saudações
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('es'), 'Glenn')
print(greet('fr'), 'Sally')
print(greet('en'), 'Michael')
# A fruitful function is one that produces a result (or return value)
# The return statement ends the function execution and 'sends back' the result of the function

#MULTIPLE PARAMETERS

def addtwo(a,b):
    added=a+b
    return added
x=addtwo(3,5)
print(x)
#output é 8
