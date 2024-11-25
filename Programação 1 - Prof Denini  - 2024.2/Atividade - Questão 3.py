# Questão 3
# Faça um programa que calcule o desconto de um produto em uma loja. Peça o valor do produto e o tipo do cliente(aposentado, estudante ou normal)

# Item a)
#   Se o cliente for aposentado, o mesmo irá receber 15% de desconto.

# Item b) 
#   Se o cliente for estudante, recebe 10% de desconto.

# Item c)
#   Se o cliente não estiver em nenhumas das situações passadas, recebe 5% de desconto.


# Entrada de dados.

print("Algoritmo para cálculo de desconto.")

tipo_cliente = str(input("Olá, você é aposentado ou estudante?"))

valor_produto = float(input("Digite o valor total do produto que você deseja comprar: "))

if tipo_cliente == "Aposentado" and "aposentado":
    valor_produtototal = valor_produto
    print(f"Você recebeu o desconto aposentado da nossa loja, seu produto total ficará: {valor_produtototal}")

elif tipo_cliente == "Estudante" and "estudante":
    valor_produtototal = valor_produto
    print(f"Você recebeu o desconto estudante! O valor total do seu produto ficará: {valor_produtototal}")

else:
    valor_produtototal = valor_produto
    print(f"Você recebeu apenas 5% de desconto da nossa loja! O valor total do seu produto ficará: {valor_produtototal}")