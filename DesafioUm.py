#entrada01 = 3.45 #(180+45=195)
#entrada02 = 14.20 #(840+20=885)
#conta = ((860 + 225)/60) - 12
#saida = 6:05

hora1 = int(input("Digite o horário em que você está: "))
minuto1 = int(input("Digite os minutos: "))
hora2 = int(input("Digite outro horario: "))
minuto2 = int(input("Digite outro minuto: "))

contaHora = (hora1+hora2)
contaMinuto = minuto1 + minuto2

if contaMinuto >= 60:
    contaHora = contaHora + 1
    contaMinuto = contaMinuto - 60

if contaHora >= 24 :
    contaHora -= 24
else:
    contaHora -= 12

#horarioFinal = ((contaHora + contaMinuto)/60) - 12

print(f"{contaHora}:0{contaMinuto}")