#Para a resolução de casos simples, esta solução é suficiente. 

#Programa de fato
entrada = input("Informe o endereço desejado: ")

endereco = entrada.split(" ")

print(endereco)

#testes com os endereços fornecidos pelo exercício
entrada = ["Miritiba 339", "Babaçu 500", "Cambuí 123B"]

for endereco in entrada:
  saida = endereco.split(" ")
  print("\n" + saida[0] + ", " + saida[1])
