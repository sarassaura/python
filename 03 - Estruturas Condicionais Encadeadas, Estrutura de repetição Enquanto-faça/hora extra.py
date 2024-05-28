'''
A jornada de trabalho semanal de um funcionário é de 40 horas. 
O funcionário que trabalhar mais de 40 horas receberá hora extra, 
cujo cálculo é o valor da hora regular com um acréscimo de 50% 
(o acréscimo de 50% ocorre apenas sobre as horas que excederem as 40 horas semanais). 
Escreva um programa que leia o número de horas trabalhadas em um mês, 
o salário por hora e escreva o salário total do funcionário, 
que deverá ser acrescido das horas extras, caso tenham sido trabalhadas. 
Considere que o mês possua 4 semanas exatas.

A saída do programa deve ser: "O salário total do funcionário é R$ S.", 
sendo S o salário em reais, mostrado com duas casas decimais.
'''

jornada_trabalho_semana = 40
jornada_trabalho_mes = 160

horas_trabalhadas_mes = int(input())

salario_hora = float(input())

horas_extras = horas_trabalhadas_mes - jornada_trabalho_mes

if horas_extras < 0:
    horas_extras = 0

salario_total = (horas_extras * salario_hora * 1.5) + ((horas_trabalhadas_mes - horas_extras) * salario_hora)

print("O salário total do funcionário é R$ {:.2f}.".format(salario_total))