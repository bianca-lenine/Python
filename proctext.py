texto = 'matemática'
# acesso por índice
print (texto[-1])
print (texto[len(texto) -1])

# repetição com for por caractere
for c in texto:
    print(c)

# Comparações entre strings
print('Matemática' == texto)
# converte para maiúscula
print(texto.upper())
print('Matemática'.upper() == texto.upper())
# converte para minúscula
print(texto.lower())
print('Matemática'.lower() == texto.lower())

# Verificar se está contida
texto = 'matemática  '
frase = "A nota de Matemática de Lucas foi 10"
# strip remove espaços 
if texto.lower().strip() in frase.lower():
    print("Achou", texto)
else:
    print("Não tá aqui")

# Particionar uma string
partes = frase.split("a")
print(partes)

# Dizer se é número
text = "78.6"
if text.replace(".", "").isdigit() == True:
    print(f"{text} é número")
else:
    print('não é número')   