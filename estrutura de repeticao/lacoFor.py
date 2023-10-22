'''
    laço for e utilizado quando sabemos  quantas vezes sera repetida
'''


for i in range(0,5):
    print(i)

'''
    no caso quando vc usar  o for vc iniciar o começo com 0 no qual ele  contado e termina com final -1
    por tanto ele so ira executar ate 4
'''

for i in range(0,5,2):
    print(f"laço 2: {+i}")

'''
    existe um terceiro parametro chamado o step no qual e opicional como vimos em exemplo anteriores
    nele vc pode decidir de quanto em quanto cada passo ate  deixar decrescente 

'''

#exemplo de interação pecorrendo um array
nomes =["jao","bao","zao","tao"]
for i in  nomes:
    print(i)
