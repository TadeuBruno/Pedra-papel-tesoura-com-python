import random
from time import sleep
print("Suas opções:")
print("[1] Pedra \n[2] Papel\n[3] Tesoura")
opcao = int(input("Sua opção: "))
lista = ["Pedra", "Papel", "Tesoura"]
escolha = random.choice(lista)
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
sleep(1)
print("-="*8)
print("Computador jogou {}".format(escolha))
if opcao == 1:
  print("Jogador1 jogou Pedra")
elif opcao == 2:
  print("Jogador1 jogou Papel")
else:
  print("Jogador1 jogou Tesoura")
print("-="*8)
if opcao == 1 and escolha == "Pedra":
    print("Empate")
elif opcao == 2 and escolha == "Papel":
    print("Empate")
elif opcao == 3 and escolha == "Tesoura":
    print("Empate")
elif opcao == 1:
  if escolha == "Papel":
    print("Computador GANHOU")
  if escolha == "Tesoura":
    print("Você GANHOU")
elif opcao == 2:
  if escolha == "Pedra":
    print("Você GANHOU")
  if escolha == "Tesoura":
    print("Computador GANHOU")
elif opcao == 3:
  if escolha == "Papel":
    print("Você GANHOU")
  if escolha == "Pedra":
    print("Computador GANHOU")