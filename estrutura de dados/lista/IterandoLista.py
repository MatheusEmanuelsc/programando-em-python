nomes=['jao','bao','zao','tao',"vao"];

# forma não ideal
for i in range(0,len(nomes)):
    print(nomes[i],i);

# forma correta porem não consegue acessar oo index
for i in nomes:
    print(i)


# forma caso precise acessar index da lista


nome = list(enumerate(nomes));

for i in nome:
    print(i)
#caso queria descompctar so  adc no adc uma nova variavel tipo i,j ai vai separar nomes do index