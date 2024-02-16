#Para os casos mais complexos, precisei de ir mais a fundo nos conceitos de expressões regulares.
#Para verificar a funcionalidade de algumas expressões utilizei o site: https://regexr.com/
#Utilizei o ArrayEntrada e o for para testes.

import re #Import da biblioteca do regex.

entrada = input("Informe o endereço desejado: ")
#ArrayEntrada = ["Miritiba 339", "Babaçu 500", "Cambuí 804B", "Rio Branco 23", "Quirino dos Santos 23 b" ,"4, Rua de la République", "100 Brodway Av", "Calle Sagasta, 26", "Calle 44 No 1991"]

#for entrada in ArrayEntrada:
saida = re.sub(r"[^\s\w]", "", entrada) # Elimina da sentença "entrada" tudo que não é "espaço", letra ou número e substitui por "vazio". 

if re.match(r"^\d", saida): #Neste caso o regex verifica se o texto começa com algum número.
  saida = re.split(r"(?<=\d)\s", saida, 1) #O regex procura um dígito numérico que seja seguido de um "espaço".
  print(saida[::-1]) #Invertendo as posições do array.

else:
  if len(re.split(r"\s(?=\d)", saida)) == 2: #Utilizei o regex para descobrir quantas posições o split possui.
    saida = re.split(r"\s(?=\d)", saida, 1) #Utilizei "\s(?=\d)" para encontrar um "espaço" seguido por algum digito númerico.
  else:
    saida = re.split(r"(?!\d)\s(?=No\s)", saida, 1) #O regex procura a palavra "espaço"No"espaço" após uma sequência de número.

  print(saida)