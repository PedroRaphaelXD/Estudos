# Questão 1 - Item (a)
# Faça um programa que leia três números inteiros e informe a soma de todos os números

# Entrada de dados com o método input restringido a números inteiro.
print("Item a - A soma de todos os números")

numero_1a = int(input("Digite apenas um número inteiro de sua escolha. Caso digite um número real, esse código irá gera um erro. Número inteiro:"))
numero_2a = int(input("Digite outro número inteiro de sua escolha: "))
numero_3a = int(input("Digite outro número inteiro de sua escolha: "))

#Soma de dados 

# Primeiro método - Sem saída de dados
# Soma através de variáveis, sem concatenação.
somatotala = numero_1a + numero_2a + numero_3a
print(f"A soma de todos os números inteiros, ditados por você, é equivalente à: {somatotala}")


# Questão 1 - item (b)
# Faça um programa que leia três números inteiros e informe o produto de todos os números

# Entrada de dados com o método input restringido a números inteiros.

print("Item b - O produto de todos os números")

numero_1b = int(input("Digite apenas um número inteiro de sua escolha. Caso digite um número real, esse código irá gera um erro. Número inteiro:"))
numero_2b = int(input("Digite apenas um número inteiro de sua escolha:"))
numero_3b = int(input("Digite apenas um número inteiro de sua escolha:"))

produtototal_1b = numero_1b * numero_2b * numero_3b

print(f"O produto total de todos os números inteiros, ditados por você, é equivalente à: {produtototal_1b}")

# Questão 2 - item (c)
# Faça um programa que leia três números inteiros e informe a média aritmética de todos os números

print("Média aritmética de todos os números.")

#Entrada de dados com o método input restringido a números inteiros.
numero_1c = int(input("Digite apenas um número inteiro de sua escolha. Caso digite um número real, esse código irá gera um erro. Número inteiro:"))
numero_2c = int(input("Digite apenas um número inteiro de sua escolha:"))
numero_3c = int(input("Digite apenas um número inteiro de sua escolha:"))

#Media airtmética utilizando-se operadores e priorização dos mesmos.
media_aritmeticac = (numero_1c + numero_2c + numero_3c )/3

#Saída de dados
print(f"A média aritmética de todos os números que você digitou, é equivalente à: {media_aritmeticac}")
