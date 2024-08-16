
notas = [7.8, 8.2, 9.5]
disciplinas = ["matemática", "português", "filosofia"]
disciplinas.append("história")
notas[0] = notas[0] + 1
notas.append(9)
#print(notas, type(notas), type(notas[0]))
print(f"A nota de {disciplinas[0]} foi {notas[0]}.")
#índice negativo lê a lista de trás para frente.
print(f"A nota de {disciplinas[-2]} foi {notas[-2]}.")
print(disciplinas[3])
print(notas[3])
#Tuplas são imutáveis, não suportam atribuição de nenhum elemento.
nomes = ["Fagundes", "Clovis", "Abismael"]
print(nomes[0], nomes[-1])