palavra = 'paralelepipedo'

for letra in palavra:
    print(letra)# o for percorre letra por letra na vertival  
print('fim')

for letra in palavra:
    print(letra,end=',')# o for percorre letra por letra na horizontal(mesma linha)   
print('fim')

aprovados = ['Rafael','Andre','Marlene']
for nome in aprovados:
    print (nome)

for posicao, nome in enumerate(aprovados):
    print(f'Posição {posicao+1})',nome)  
    
dias = ('Domingo', 'Segunda-feira', 'Terça-feira', 
        'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado')    
i = 1        
for dia in dias:
    print(f'Dia: {dia}')        