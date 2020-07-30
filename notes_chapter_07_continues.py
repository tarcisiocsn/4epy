#PROMPT FOR FILE NAME - procurar a partir do nome do arquivo
fname=input('Enter the file Name: ')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('Subject'):
        count=count+1
print('There were', count, 'Subject lines in', fname)

#BAD FILES NAMES
fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened', fname)
    quit()
count=0
for line in fhand:
    if line.startswith('Subject'):
        count=count+1
print('There were', count, 'Subject lines in', fname)
