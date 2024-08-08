nota = 5
media_alta = 7
media_baixa = 5

if nota >= media_alta:
    print("Aprovado direto!😎") 
elif nota >= media_baixa:
    print("Fazer prova final.")
    nota_pf = 3
    if nota_pf >= media_baixa:
        print("Aprovado na prova final!")
    else:
        print("Prova de recuperação final.")
        nota_rf = 5
    if nota_rf >= media_baixa:
        print("Aprovado na recuperação!")
    else:
        print("REPROVADO.")  
else:
    print("Fazer recuperação final 😱")
    nota_rf = 5
    if nota_rf >= media_baixa:
        print("Aprovado na recuperação!")
    else:
        print("REPROVADO.")    
    