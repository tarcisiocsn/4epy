fh=open('mbox-short-2.txt')
print(fh)
for lx in fh:
    ly=lx.rstrip() #vai tirar as new lines \n que já contem e ficará como o arquivo original, pq python ele acrescenta de novo uma nova linhas
    lz=ly.upper()
    print(lz) #o loop será - lerá todas as linhas em fh
#FICOU LINDO PAPAPAAAAAAI!!!!!!

#PODERIA SER TBM PRINT(LY.UPPER())
