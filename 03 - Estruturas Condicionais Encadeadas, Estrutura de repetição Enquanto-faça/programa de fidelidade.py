'''
O programa de fidelidade de uma empresa premia seus clientes com descontos em 
novas compras de acordo com a categoria do cliente (prata ou ouro) e 
com o valor de suas compras, segundo a tabela a seguir.

Image: https://drive.google.com/file/d/1RonM17XQtiVt8X_ZIER7-FMUOPWfpHfc/view?usp=drive_link

Elabore três funções para determinar 
o valor final a ser pago por um cliente participante do programa de fidelidade desta empresa. 
A primeira função, chamada de clientePrata, 
recebe o valor da compra feita por um cliente nível Prata e 
retorna o valor (em R$) do desconto que será aplicado. 
A segunda função, chamada de clienteOuro, 
recebe o valor da compra feita por um cliente nível Ouro e 
retorna o valor (em R$) do desconto que será aplicado. 
A terceira função, chamada de gerenciaClientes, 
recebe a informação sobre o nível do cliente (Prata ou Ouro) e 
o valor da compra realizada e retorna tanto o desconto aplicado como 
o valor final da compra após os descontos. 
Esta última função deve usar as duas primeiras em seu código.
'''

def clientePrata(v):
  if v < 150.01:
    return v
  elif (v >= 150.01) and (v <= 300.00):
    return v * 1.5 / 100
  elif (v >= 300.01) and (v <= 600):
    return v * 2.5 / 100
  elif (v >= 600.01) and (v <= 1000):
    return v * 3.5 / 100
  elif (v >= 1000.01) and (v <= 2000):
    return v * 4.5 / 100
  else:
    return v * 4.5 / 100

def clienteOuro(v):
  if v < 150.01:
    return v
  elif (v >= 150.01) and (v <= 300.00):
    return v * 2.5 / 100
  elif (v >= 300.01) and (v <= 600):
    return v * 3.5 / 100
  elif (v >= 600.01) and (v <= 1000):
    return v * 4.5 / 100
  elif (v >= 1000.01) and (v <= 2000):
    return v * 5.5 / 100
  else:
    return v * 6 / 100

def gerenciaClientes(nivel, v):
  if nivel == "Prata":
    D = clientePrata(v)
    final = v - D
    return D, final
  elif nivel == "Ouro":
    D = clienteOuro(v)
    final = v - D
    return D, final