#Equilátero: Todos os lados são iguais.
#Isósceles: Dois lados são iguais.
#Escaleno: Todos os lados são diferentes.

ladoA = float(input("Informe o comprimento do primeiro lado:"))
ladoB = float(input("Informe o comprimento do segundo lado:"))
ladoC = float(input("Informe o comprimento do terceiro lado:"))

if ladoA == ladoB == ladoC:
    print("O triângulo é equilátero.")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC: 
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")