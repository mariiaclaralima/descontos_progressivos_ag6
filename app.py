 
  #Programa de cálculo de desconto progressivo
#Autor: Maria Clara Lima

#Entrada
valor_inicial= float(input("Digite o valor total, em reais, da sua compra: "))

#Processamento
if valor_inicial >=300:
    desconto= valor_inicial*(0.15)
elif valor_inicial >=200:
    desconto= valor_inicial*(0.1)
else:
    desconto= valor_inicial*(0.05)

valor_final= valor_inicial-desconto

#Saída
print("Na sua compra de R$", valor_inicial, ", você adquiriu um desconto de R$", desconto, "! Logo, o valor final da sua compra será de R$", valor_final)