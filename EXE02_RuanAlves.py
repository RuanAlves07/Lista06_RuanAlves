#EXE 002 - Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.

produtos = ("Maça", "Banana","Pera","Uva","Arroz","Farinha","Ovo","Frango","Carne","Macarrão")

print(produtos)

pergunta = input("Escolha um dos produtos acima: ")

if pergunta in produtos:
        escolha_produto = produtos.index(pergunta)
        print("Posição do produto: {}".format(escolha_produto))
    
pergunta2 = int(input("Escolha de 0 a 9 para exibir o produto: "))

if pergunta2 < len(produtos):
    
    print("Produto: {}".format(produtos[pergunta2]))    

print("Ruan Augusto Alves")   


