# Programa para calcular o fatorial de um número usando while

while True:
    # Solicita ao usuário um número inteiro
    numero = int(input("Informe um número inteiro: "))
    
    if numero == 0:
        print("O número tem que ser positivo.")
        break  # Sai do loop se o número for 0

    # Inicializa a variável para armazenar o resultado do fatorial
    resultado = 1

    # Calcula o fatorial
    i = 1
    while i <= numero:
        resultado *= i  # Multiplica o resultado pelo contador
        i += 1  # Incrementa o contador

    # Exibe o resultado
    print(f"O fatorial de {numero} é: {resultado}")