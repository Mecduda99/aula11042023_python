# Pomodoro timer 'fake'
contador = 0
timer = int(input('quanto tempo você deseja para estudar?'))
intervalo = timer / 2

while contador <= timer:
  if contador == 0:
    print("iniciando contagem...")

  if contador == intervalo:
    print("Parabéns, você completou o primeiro tempo!")
    print("Faça uma pausa de 5 minutos.")
    continuar = input("Você deseja continuar? S/N ")
    if continuar == "N":
      print("contador finalizado no tempo:" + str(contador) + ":00")
      break
    if continuar == "S":
      print("Ótimo! Vamos lá.")
  print("Tempo: " + str(contador) + ":00")

  if contador == timer:
    print("Parabéns!! Você finalizou o seu tempo de estudos diário.")
  contador += 1

    