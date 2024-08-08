media = int(input("Digite a média:"))
nota = input("Digite a nota:")
nota = float(nota)

if nota >= media:
    print("Aprovado com nota", nota)
else: 
    print("Reprovado com nota", nota, "(a média é", media,")")

