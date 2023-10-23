'''
    E uma outra estrutura de dados 
    que pode guardar atraves de  chaves os  valores

    dicionario tudo dentro de chaves
'''

# criando um dicionario
nome ={"nome":"jao","sobrenome":"bao"}
# oque ta a esqueda sera chave e direita o valor 

# acessando valores
print(nome)

#acessando uma unica posição
print(nome["nome"])

#criando dicionario com lista

x = {'nomes':[],'seilar':'podeser'}
# uma lidta no python como vc sabe e tudo dentro de  []

# adc valores

x["nomes"].append('jao')
x["nomes"].append('bao')
print(x["nomes"])


#criando chaves que não foram predefinidas

nome['numero'] ='12345'
print(nome)
#caso não exista ela vai criar uma nova chave

# outra forma
nome.update({'id':'123'})
print(nome)
#caso queria adc mais basta adc por a virgular ',' e seguir o mesmo processo chave e valor