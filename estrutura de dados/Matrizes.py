# Lista podem ter lista dentro dela  chamando assim  de matriz
#para ser um matriz deve ter a mesma quantidade de coluna
#porem no python e permitido ter numeros colunas diferentes

num = [

    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]

]

print(num[1][3]) #acessando matriz


#Iterando

for i  in range(0,len(num)):
    for j in range(0,len(num[1])):
        print(num[i][j])