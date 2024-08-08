nota = float(input("Informe a nota:"))

if nota >= 9:
    print("A", nota, "corresponde ao conceito A")
elif nota >= 8 and nota < 9:
    print("A", nota, "corresponde ao conceito B")
elif nota >= 7 and nota < 8:
    print("A", nota, "corresponde ao conceito C")
elif nota >= 6 and nota < 7:
    print("A", nota, "corresponde ao conceito D")
else:
    print("A", nota, "corresponde ao conceito F")
    

