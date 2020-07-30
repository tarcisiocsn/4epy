fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
    
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not '@uct.ac.za' in line: #negocio é: se não tem esse usuario skip it e print apenas o que tem
        continue
    print(line)
