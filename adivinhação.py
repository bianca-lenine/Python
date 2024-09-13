import random
resposta = random.randint(1,20)
while True:
    n = float(input("Chute um número de 1 a 20: "))
    
    if n > resposta:
        print("opss, esse número é MAIOR do que a resposta")
    elif n < resposta:
        print("opss, esse número é MENOR do que a resposta")
    else:
        print("VOCÊ ACERTOU!!!")
        break
        



