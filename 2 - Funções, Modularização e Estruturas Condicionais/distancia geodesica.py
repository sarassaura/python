'''
A distância geodésica é a maneira pela qual 
se obtém a menor distância entre dois pontos em um superfície curva. 
Considerando a superfície da terra, 
qualquer ponto nessa superfície pode ser dado por coordenadas de latitude (lat) e longitude(lon). 
Escrevendo essas coordenadas em graus graus decimais, 
o cálculo da distância geodésica entre dois pontos (lat1,lon1) e (lat2,lon2) 
envolve os seguintes passos, que levam ao método de Haversine:

Primeiramente, converter todos os valores das latitudes e longitudes 
(considerando os dois pontos) de graus decimais c(d) para radianos c(rad), 
usando a fórmula:

c(rad) = c(d) * π / 180


Depois, deve-se usar os valores em radianos 
para obtenção dos módulos dos valores das diferenças das coordenadas 
tanto das latitudes como das longitudes, usando a seguinte fórmula:

Δc = |c(rad1) - c(rad2)|

em que Δc é o módulo das diferenças dos valores das coordenadas; 
c(rad1) e (crad2) são os valores das coordenadas dos dois pontos 
considerando-se latitudes ou longitudes em radianos. 
Essa formulação pode ser usada para a obtenção de ΔLat, 
que é o módulo da diferença entre as latitudes, e 
ΔLon, que é o módulo da diferença entre as longitudes.

A partir desses valores, 
além dos valores das latitudes (em radianos) dois dois pontos, 
deve-se calcular o parâmetro A, dado pela equação a seguir:

A=(sen(ΔLat/2)^2+cos(lat1))*cos(lat2)*sen(ΔLon/2)^2

Então, calcula-se o parâmetro B, 
que utiliza a função de arco-tangente (tan^(-1)) a partir de A:

B = 2 * tan^(-1) * (√A/(√1-A))

Finalmente, o parâmetro B é usado para calcular a distância geodésica (D) 
a partir do conhecimento do raio da terra R, que equivale a 6371 km:

D = B * R


A partir desses passos, escreva três funções: coordec2rad, 
que converte coordenadas em graus decimais (entrada) para radianos (saída); 
deltaCoord, que calcula o módulo da diferença de coordenadas e 
será usada para a obtenção de ΔLat e ΔLon 
(essa função retorna o módulo da diferença e recebe as latitudes ou longitudes em radianos); e 
distGeodesica, que vai retornar a distância geodésica entre dois pontos situados no globo terreste, 
a partir de suas coordenadas de latitudes e longitudes (dos dois pontos geográficos) 
escritas em graus decimais, além do raio da Terra (R). 
Esta última função necessariamente terá que usar as duas primeiras (coordec2rad e deltaCoord) internamente.

Você pode usar o valor de pi (use np.pi), 
extrair a raiz quadrada (use o comando np.sqrt), 
calcular senos (np.sin) e cossenos (np.cos), 
bem como calcular o arco-tangente (np.arctan). 
O módulo matemático também pode ser obtido usando o comando np.abs.

Image: https://drive.google.com/file/d/1YTvG9Aaked8i3YUGavbt68iorqI1f_2N/view?usp=drive_link
'''

import math

def coordec2rad(d):
  return (d * math.pi) / 180

def deltaCoord(c1, c2):
  return abs(coordec2rad(c1) - coordec2rad(c2))

def distGeodesica(lat1, lon1, lat2, lon2, R):
  delta_lat = deltaCoord(lat1,lat2)
  delta_lon = deltaCoord(lon1,lon2)

  A = ((pow(math.sin(delta_lat / 2), 2)) + (math.cos(coordec2rad(lat1)))) * math.cos(coordec2rad(lat2)) * (pow(math.sin(delta_lon / 2), 2))
  B = 2 * math.atan(pow(A,0.5) / pow((1 - A), 0.5))
  D = B * R
  return D