#%%
lista =  [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = input("Entre com um número: ")
numero = int(numero)

contador = 0
for i in lista:
    if i == numero:
        contador +=1

print("Quantidade de:", numero, ":", contador)
 
""" 
Nesse código, foi feito uma lista contendo números, logo após,
foi solicitado para que o usuário entrasse com um número.

O código pega esse número e o transforma em inteiro. Após isso,
foi criado um contador que starta no 0, o for serve pra verificar os
números presentes na lista, o IF pega o número que o usuário digitou e
verifica se tem esse mesmo número na lista, caso tenha, adiciona
+1 no contador. Depois o código informa a quantidade do número que
o usuário digitou.




"""

