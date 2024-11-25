#Questão 2 - Atividade 1 
# Faça um programa que peça ao usuário a largura e o comprimento de um terreno retangular e calcule a área e o perímetro desse terreno.

print("Cálculo da área de um terreno.")


# Entrada de dados - Área.

largura = float(input("Digite a largura do terreno sem a unidade de medida: "))
comprimento = float(input("Digite o comprimento do terreno sem a unidade de medida: "))

area_terreno = largura * comprimento


#Saída de dados - Resultado da área
print(f"A área total do seu terreno é equivalente á: {area_terreno}")

# Perímetro terreno - Formação de dados

#Cálculo do perimetro do terreno apartir de dados já informados pelo usuário.
perimetro_terreno = (comprimento * 2) + (largura * 2)

#Saída de dados - Resultado do perímetro.
print(f" O perimetro total do seu terreno é equivalente à: {perimetro_terreno}")


