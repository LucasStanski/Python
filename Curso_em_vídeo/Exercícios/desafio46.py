import emoji
from time import sleep
print("Preparado para a virada de ano? ")
print("Que comece os fogos em: ")
for c in range(10, 0, -1):
    sleep(1)
    if c==1:
        print("1")
    elif c==2:
        print("2")
    elif c==3:
        print("3")
    elif c==4:
        print("4")
    elif c==5:
        print("5")
    elif c==6:
        print("6")
    elif c==7:
        print("7")
    elif c==8:
        print("8")
    elif c==9:
        print("9")
    else:
        print("10")
print(emoji.emojize("Feliz ANO NOVO!!! 🎆🎇🎆🎉🎆🎊🎆🎆✨"))