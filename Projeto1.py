#Agora, para resolver casos mais complexos, fiz uso do RegExr, visto que é mais agradável para lidar com Strings.
#Neste caso, o que fiz foi encontrar um "espaço" seguido por algum digito númerico "\s(?=\d)" e realizar um split nesse "espaço" em questão.

import re

# Como funcionaria o programa na prática
ruas = input("Informe o endereço desejado: ")

resultado = re.split(r"\s(?=\d)", ruas) #Realiza um split em um local onde há um "espaço seguido por um dígito numérico."
print(resultado)

#testes com os endereços do exercício
Array_ruas = ["Rio Branco 23", "Quirino dos Santos 23 b"]

for entrada in Array_ruas:
  saida = re.split(r"\s(?=\d)", entrada)

  print(saida[0])
  print(saida[1])
