#-*- coding:UTF-8 -*-

print("olá mundo! Vamos analisar se um número é primo ou não!")

num1 = int(input("Me de um número"))
def primo(num1):
        cont = 0  
        for i in range(1, num1):
                if num1 % i == 0:
                        cont += 1 
        if cont == 1:
                print("o número é primo!")
        else:
                print("o número não é primo")
primo(num1)

