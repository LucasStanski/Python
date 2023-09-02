import random
aleatorio=random.randint(1,100)
largura=35
enchimento=" "
print("\033[33m*\033[m"*34)
print("\033[97mBem vindo a um jogo de adivinhação,\033[m")
print("\033[97mO jogo consiste em acertar o número\033[m")
print("\033[97mde 0 a 100, tenha uma boa sorte!!!\033[m")
print("\033[33m*\033[m"*34)
tentativas=0
print("\033[97mNíveis de dificuldade \033[m")
print("\033[97m[1] Difícil 5 Tentativas\033[m")
print("\033[97m[2] Médio   10 Tentativas\033[m")
print("\033[97m[3] Fácil   20 Tentativas\033[m")
nivel_ecolhido=int(input("\033[97mQual nível irá escolher? \033[m"))
print("\033[33m*\033[m"*34)
if nivel_ecolhido==1:
    tentativas=5
elif nivel_ecolhido==2:
    tentativas=10
else:
    tentativas=20
for rodada in range(1, tentativas+1):
    if rodada==1:
        print("\033[34mPrimeira tentativa\033[m".center(largura, enchimento))
    if rodada==2:
        print("\033[34mSegunda tentativa\033[m".center(largura, enchimento))
    if rodada==3:
        print("\033[34mTerceira tentativa\033[m".center(largura, enchimento))
    if rodada==4:
        print("\033[34mQuarta tentativa\033[m".center(largura, enchimento))
    if rodada==5:
        print("\033[34mQuinta tentativa\033[m".center(largura, enchimento))
    if rodada==6:
        print("\033[34mSexta tentativa\033[m".center(largura, enchimento))
    if rodada==7:
        print("\033[34mSétima tentativa\033[m".center(largura, enchimento))
    if rodada==8:
        print("\033[34mOitava tentativa\033[m".center(largura, enchimento))
    if rodada==9:
        print("\033[34mNona tentativa\033[m".center(largura, enchimento))
    if rodada==10:
        print("\033[34mDécima tentativa\033[m".center(largura, enchimento))
    if rodada==11:
        print("\033[34mDécima Primeira tentativa\033[m".center(largura, enchimento))
    if rodada==12:
        print("\033[34mDécima Segunda tentativa\033[m".center(largura, enchimento))
    if rodada==13:
        print("\033[34mDécima terceira tentativa\033[m".center(largura, enchimento))
    if rodada==14:
        print("\033[34mDécima Quarta tentativa\033[m".center(largura, enchimento))
    if rodada==15:
        print("\033[34mDécima Quinta tentativa\033[m".center(largura, enchimento))
    if rodada==16:
        print("\033[34mDécima Sexta tentativa\033[m".center(largura, enchimento))
    if rodada==17:
        print("\033[34mDécima Setima tentativa\033[m".center(largura, enchimento))
    if rodada==18:
        print("\033[34mDécima Oitava tentativa\033[m".center(largura, enchimento))
    if rodada==19:
        print("\033[34mDécima Nona tentativa\033[m".center(largura, enchimento))
    if rodada==20:
        print("\033[34mVigésima tentativa\033[m".center(largura, enchimento))
    numero_Jogador=int(input("\033[97mDigite o seu número da sorte: "))
    n1=numero_Jogador==aleatorio
    n2=numero_Jogador<aleatorio
    n3=numero_Jogador>aleatorio
    if n1:
        print("\033[35mVocê acertou!!!\033[m")
        break
    else:
        if n2:
            print("\033[97mVocê errou!!!\033[m")
            print("\033[32mDICA:\033[m \033[97mO valor que digitou é muito baixo\033[m")
            print("\033[33m*\033[m"*39)
        elif n3:
            print("\033[97mVocê errou!!!\033[m")
            print("\033[32mDICA:\033[m \033[97mO valor que digitou é muito alto\033[m")
            print("\033[33m*\033[m"*39)
print("\033[1;30;107mMuito obrigado por participar!!!\033[m")
