nomes=['jao','bao','zao','tao',"vao"];
print(nomes);


#alterando apenas um valor
nomes[0]="Jao";

# adicionando elementos no final da lista
nomes.append('gab');
nomes.append('tai');

print(nomes);

#Inserindo elementos diferente append que adc ao final insert precisa de dois parametros o valor e a posição desejada
nomes.insert(6,"kai");
print(nomes);


# Removendo um valor pop por padrão remove o ultimo valor da lista

nomes.pop()
print(nomes)

# caso vc queira remover um que não estva no final basta pop e a posição
nomes.pop(4);
print(nomes)

# caso vc  queria remover  com base no valor utilize  remove
# se tiver mais de um valor ele remove o primeiro valor que encontra
nomes.remove("tao");
print(nomes)

# descobrindo index
# ele funciona como remove no caso quem ele encontra primeiro retorna a posiçao
print(nomes.index("Jao"));

