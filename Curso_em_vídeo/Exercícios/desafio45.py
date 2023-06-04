import random
from time import sleep
maquina=random.randint(1,3)
print("\033[36m*\033[m"*25)
print("\033[33mBem vindo ao jogo Jokenpô\033[m")
print("\033[36m*\033[m"*25)
print("\033[33m[1] Pedra\033[m")
print("\033[33m[2] Papel\033[m")
print("\033[33m[3] Tesoura\033[m")
pessoa=int(input("\033[33mEscolha uma das opções: \033[m"))
print("\033[36m*\033[m"*25)
print("\033[33mJo\033[m")
sleep(1)
print("\033[33mKen\033[m")
sleep(1)
print("\033[33mPô!!!\033[m")
sleep(1)
if pessoa==1:
    print("\033[33mJogador jogou Pedra\033[m")
if pessoa==2:
    print("\033[33mJogador jogou Papel\033[m")
if pessoa==3:
    print("\033[33mJogador jogou Tesoura\033[m")
if maquina==1:
    print("\033[33mMaquina jogou Pedra\033[m")
if maquina==2:
    print("\033[33mMaquina jogou Papel\033[m")
if maquina==3:
    print("\033[33mMaquina jogou Tesoura\033[m")
print("\033[36m*\033[m"*25)
if maquina==pessoa:
    print("\033[33mO jogo empatou\033[m")
#PEDRA e PAPEL
if pessoa==1 and maquina==2:
    print("\033[33mMaquina ganhou\033[m")
    print("\033[33mMaquina embrulhou a pedra, de Jogador\033[m")
if pessoa==2 and maquina==1:
    print("\033[33mJogador ganhou\033[m")
    print("\033[33mJogador embrulhou a pedra, de Maquina\033[m")
#PEDRA E TESoURA
if pessoa==1 and maquina==3:
    print("\033[33mJogadou ganhou\033[m")
    print("\033[33mJogador quebrou a tesoura, de Maquina\033[m")
if pessoa==3 and maquina==1:
    print("\033[33mMaquina ganhou\033[m")
    print("\033[33mMaquina quebrou a tesoura, de Jogador\033[m")
#TESOURA e PAPEL
if pessoa==3 and maquina==2:
    print("\033[33mJogador ganhou\033[m")
    print("\033[33mJogador cortou o papel de Maquina\033[m")
if pessoa==2 and maquina==3:
    print("\033[33mMaquina ganhou\033[m")
    print("\033[33mMaquina cortou o papel de Jogador\033[m")
print("\033[33mObrigado por ter jogado <3\033[m")
