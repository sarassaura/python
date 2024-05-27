'''
Faça um programa que, dado o valor total de uma compra, 
em reais, e o número de prestações desejadas, 
calcule o valor de cada parcela do pagamento. 

Para pagamento à vista (1 parcela), 
seu programa deve prever um desconto de 2% no valor da compra. 
Neste caso, a mensagem será: "Compra de R$ V à vista. 
Valor cobrado: R$ D.", em que V é o valor total da compra, 
com duas casas decimais e D é o valor  pago pelo cliente, 
considerando o desconto, com duas casas decimais.

Para que a compra tenha um parcelamento sem juros, 
o número máximo de parcelas é deve ser entre 2 e 6. 
Entre 7 e 12 parcelas devem ser acrescidos juros de 
6.0, 6.5, 7.0, 7.5, 8.0 e 8.5%, respectivamente, 
de acordo com o número de parcelas escolhido. 
Neste caso, seu programa deve prover a seguinte mensagem: 
"Compra de R$ V, parcelada em X parcelas. 
Valor de cada parcela: R$ P.", 
em que V é o valor total da compra, com duas casas decimais; 
X é o número de parcelas e 
P é o valor  de cada parcela, com duas casas decimais.

Seu programa deve ainda prever o tratamento de dados 
para o caso em que o número de parcelas seja 
menor que um ou maior que 12. 
Nessas circunstâncias o programa deve 
apenas emitir a seguinte mensagem de erro: 
"O número de parcelas deve ser maior que zero e menor ou igual a 12.".

Veja exemplos dos testes que serão realizados: 

ENTRADAS 1

1000
2

SAÍDA 1

Compra de R$ 1000.00, parcelada em 2 parcelas. Valor de cada parcela: R$ 500.00.

ENTRADAS 2

2500
8

SAÍDA 2

Compra de R$ 2500.00, parcelada em 8 parcelas. Valor de cada parcela: R$ 332.81.
'''

compra = float(input())
prestacoes = int(input())
parcela = 0

if prestacoes == 1:
  parcela = compra * 0.98
  print("Compra de R$ {:.2f} à vista. Valor cobrado: R$ {:.2f}.".format(compra, parcela))
elif prestacoes >= 2 and prestacoes <= 6:
  parcela = compra / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
elif prestacoes == 7:
  depois = compra * 1.06
  parcela = depois / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
elif prestacoes == 8:
  depois = compra * 1.065
  parcela = depois / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
elif prestacoes == 9:
  depois = compra * 1.07
  parcela = depois / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
elif prestacoes == 10:
  depois = compra * 1.075
  parcela = depois / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
elif prestacoes == 11:
  depois = compra * 1.08
  parcela = depois / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
elif prestacoes == 12:
  depois = compra * 1.085
  parcela = depois / prestacoes
  print("Compra de R$ {:.2f}, parcelada em {:d} parcelas. Valor de cada parcela: R$ {:.2f}.".format(compra, prestacoes, parcela))
else:
  print("O número de parcelas deve ser maior que zero e menor ou igual a 12.")