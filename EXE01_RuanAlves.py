#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.


paises = ('Brasil, Peru, Chile, Colombia, Argentina')
print(paises)

pergunta = input("Insira um dos paises da tupla: ")

if pergunta in paises:
    country = paises.index(pergunta)
    print("O país que você escolheu é o: {} e o índice do mesmo é o: {}".format(pergunta, country))
else:
    print("O país selecionado não está na lista!")

print ("Ruan Augusto Alves")

