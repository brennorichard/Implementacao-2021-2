import statistics
from time import sleep
def tend_cent(dado):
    dad=[]
    cont=0
    while dados> cont:
      numero =float(input(f'digite o numero {cont+1}° '))
      dad.append(numero)
      cont+=1
    dad_ord= sorted(dad)
    qd=(len(dad))
    #media
    tot=0
    for dado in dad:
      tot+= dado
    print(f'\nMédia: {tot/qd}')
    #moda
    moda= statistics.mode(dad)
    y=0
    z=0
    for x in dad:
     if  moda == dad[y]:
        z+=1
        if z >= 2:
            print (f'Moda: {moda}')
            break
        y+=1
    if z<2:
        print('Não existe uma moda')

  #mediana
    if qd%2 == 0:
        meio=int(qd/2)
        med1=dad_ord[meio-1]
        med2=dad_ord[meio]
        meiomed=(med1+med2)/2
        print(f'mediana:{meiomed}')
    else:
      med=int(((qd+1)/2)-1)
      medf=dad_ord[med]
      print(f'mediana:{medf}\n')
def media_pon(dado):
      nota=0
      peso=0
      cont=0
      while dados>cont:
          nota_d = float(input(f'digite o numero {cont+1}°: '))
          peso_d = float(input(f'digite o peso {cont+1}°: '))
          nota = nota +(nota_d * peso_d)
          peso = peso + peso_d
          cont+=1
      print(f'A media ponderada é igual a {nota/peso}\n')
def media_geo(dado):
    cont=0
    num=1
    while dados > cont:
        numero =float(input(f'digite o numero {cont+1}° '))
        num = num * numero
        cont+= 1
    print(f'A média geometrica é igua a {num**(1/dados)}\n')


def med_disp(dados):
    cont=0
    L1 = []
    while dados > cont:
        numero =float(input(f'digite o numero {cont+1}° '))
        L1.append(numero)
        cont+=1
        tamanho=len(L1)
    #amplitude
    ampmaior=max(L1)
    ampmenor=min(L1)
    print(f'O maior valor é {ampmaior} e o menor valor é de {ampmenor} e a amplitude é de {ampmaior-ampmenor}')
    #desvio
    desvio=0
    totnot=sum(L1)
    med =totnot/tamanho
    while desvio < tamanho:
        nova_lis= int(L1[desvio])- med
        print(f'Desvio {desvio+1} = {nova_lis}')
        desvio+=1
    #variancia

    cont1=0
    variavel=0
    while cont1 < tamanho:
        var_lis= ((int(L1[cont1])- med)**2)
        cont1+=1
        variavel= variavel+var_lis
    resultvar = variavel/tamanho
    print(resultvar)




print("╭━━━━-╮\n╰┃ ┣▇━▇\n┃ ┃  ╰━▅╮\n╰┳╯ ╰━━┳╯\n╰╮ ┳━━╯\n▕▔▋ ╰╮╭━╮ \n╱▔╲▋╰━┻┻╮╱-╲\n▏  ▔▔▔▔▔O O┃\n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n▏╳▕▇▇▕ ▏╳▕▇▇▕\n╲▂╱╲▂╱ ╲▂╱╲▂╱\n")
print("====DOG CALCULATOR====")


cond=True
while cond == True:
    print('-'*25)
    print('|opções de calculo:     |\n|(1)tendencia central   |\n|(2)media ponderada     |\n|(3)media geometrica    |\n|(4)medidas de dispersão|')
    print('-'*25)
    op = float(input('\ndigite uma opção de calculo: '))
    while op>4 or op<1:
        print ('Numero invalido digite novamente...')
        op = float(input('digite uma opção de calculo: '))
    dados=int(input('digite a quantidade de dados totais: '))

    #tendencia central
    if op == 1:
        tend_cent(dados)
    #media ponderada
    if op == 2:
        media_pon(dados)
    #media geometrica
    if op ==3:
        media_geo(dados)
    if op ==4:
        med_disp(dados) 
    
    res=str(input('Deseja continuar? (S/N): ')).upper()
    cond2= False
    if res == 'S' or res == 'N':
        cond2= True
    while cond2 == False:
        print('Resposta diferente da padrão favor digitar novamente')
        res=str(input('Deseja continuar? (S/N): ')).upper()
        print (res)
    if res == 'S':
        cond= True
    else:
        cond= False
