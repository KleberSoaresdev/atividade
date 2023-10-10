contagem = 1
saida = []
impar = 1
while contagem <11:
    saida.append(impar)
    impar += 2
    contagem +=1
print(saida)
#correção da atividade em sala:
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
impar = 0
cont = 0
while True:
    if cont%2 !=0:
        c[impar]=cont
        impar=impar+1
    cont=cont+2
    if impar >=10:
        break
