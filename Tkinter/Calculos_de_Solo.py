from Tkinter import *
import os
janela=TkinterTk()
janela.title("Necessidade de calcario")
largura=321
altura=326
janela.resizable(False,False)
largura_screen=janela.winfo_screenwidth()
altura_screen=janela.winfo_screenheight()
posx=largura_screen/2-largura/2
posy=altura_screen/2-altura/2
janela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
 
def Soma_de_Bases():
    ca = float(e_ca.get())
    mg = float(e_mg.get())
    k = float(e_k.get())
    na = float(e_na.get())
    sb=ca+mg+k+na
    resultado=sb
    result["text"]="{:.{}f}".format(resultado,2)
def CTC():
    ca = float(e_ca.get())
    mg = float(e_mg.get())
    k = float(e_k.get())
    na = float(e_na.get())
    h_al = float(e_h_al.get())
    sb=ca+mg+k+na
    ctc=sb+h_al
    resultado=ctc
    result["text"]="{:.{}f}".format(resultado,2)
def v1():
    ca = float(e_ca.get())
    mg = float(e_mg.get())
    k = float(e_k.get())
    na = float(e_na.get())
    h_al = float(e_h_al.get())
    sb=ca+mg+k+na
    ctc=sb+h_al
    v1=sb*100/ctc
    resultado=v1
    result["text"]="{:.{}f}".format(resultado,2)
def nc():
    ca = float(e_ca.get())
    mg = float(e_mg.get())
    k = float(e_k.get())
    na = float(e_na.get())
    h_al = float(e_h_al.get())
    sat_bas = float(e_v2.get())
    prnt = float(e_prnt.get())
    sb=ca+mg+k+na
    ctc=sb+h_al
    v1=sb*100/ctc
    nc=(sat_bas-v1)*ctc/prnt
    resultado=nc
    result["text"]="{:.{}f}t/ha".format(resultado,2)

pastaApp=os.path.dirname(__file__)
Imagem=PhotoImage(file=pastaApp+"\\Grafic.png")
labelimagme=Label(janela, image=Imagem)
labelimagme.place(x=0,y=0)

result=Label(janela,font="TimesNewRoman 15",text="---")
result.place(width=55,height=23,x=222,y=27)

b_Sb=Button(janela, command=Soma_de_Bases, text="SB",font="Arial 12 bold",justify=CENTER)
b_Ctc=Button(janela, command=CTC, text="CTC",font="Arial 12 bold",justify=CENTER)
b_nc=Button(janela, command=nc, text="NC",font="Arial 12 bold",justify=CENTER)
b_v2=Button(janela, command=v1, text="V1",font="Arial 12 bold",justify=CENTER)

b_Sb.place(width=36,height=17,x=220,y=63)
b_Ctc.place(width=36,height=17,x=260,y=63)
b_nc.place(width=36,height=17,x=220,y=93)
b_v2.place(width=36,height=17,x=260,y=93)

e_ca=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)
e_mg=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)
e_k=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)
e_na=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)
e_h_al=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)
e_prnt=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)
e_v2=Entry(janela,font="TimesNewRoman 15 bold",justify=CENTER)

e_ca.place(width=55,height=23,x=74,y=27)
e_mg.place(width=55,height=23,x=74,y=71)
e_k.place(width=55,height=23,x=74,y=114)
e_na.place(width=55,height=23,x=74,y=159)
e_h_al.place(width=55,height=23,x=74,y=202)
e_prnt.place(width=55,height=23,x=74,y=246)
e_v2.place(width=55,height=23,x=74,y=290)

janela.mainloop()
