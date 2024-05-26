'''
Faça um programa para ler 2 coordenadas geográficas válidas: 
uma de latitude e uma de longitude. 
A coordenada de latitude, escrita em graus decimais, 
deve estar no intervalo [-90,90] e 
a coordenada de longitude, também escrita em graus decimais, 
deve estar no intervalo [-180, 180]. 
Seu programa deve primeiramente ler a coordenada de latitude 
até que uma coordenada válida seja obtida. 
Sempre que o usuário entrar com uma coordenada não válida 
seu programa deve emitir a mensagem de erro: 
"A coordenada de latitude não é válida!". 
Depois, seu programa deve fazer a leitura 
de uma coordenada válida de longitude, 
sendo que para o caso de não ser uma coordenada válida, 
a mensagem de erro será: 
"A coordenada de longitude não é válida!" 
Com as duas coordenadas válidas, 
seu programa deve mostrá-las com o seguinte formato: 
"As coordenadas digitadas foram: (lat,lon)", 
em que lat é a coordenada de latitude, 
com duas casas decimais, e lon é a coordenada de longitude, 
também com 2 casas decimais. 
Seu programa deve ser construído com a estrutura de repetição while. 
'''

while True:
  latitude = float(input())
  if (latitude < -90) or (latitude > 90):
    print("A coordenada de latitude não é válida!")
    continue
  break

while True:
  longitude = float(input())
  if (longitude < -180) or (longitude > 180):
    print("A coordenada de longitude não é válida!")
    continue
  break

print("As coordenadas digitadas foram: ({:.2f},{:.2f})".format(latitude, longitude))