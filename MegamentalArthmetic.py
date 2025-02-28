from time import sleep as sl
from os import system as sy
from random import randint as ra
soma = 0
save = 0
sy("cls")
str(input('Digite "enter" para começar o desafio\n'))
for i in range (1, 100):
    sy("cls")
    save = (ra(1000, 9999))
    print(save)
    soma += save
    sl(0.3)
sy("cls")
if int(input("Digite o resulltado: ")) == soma:
    print("\n\033[32mO RESULTADO ESTÁ CORRETO!\033[m")
else:
    print("\n\033[31mO RESULTADO ESTÁ INCORRETO!\033[m")
