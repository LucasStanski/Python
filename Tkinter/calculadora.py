import Tkinter
branca = "#feffff"
azul = "#38576b"  
cinza ="#ECEFF1"
laranja="#FFAB40"
preto="#3b3b3b"

janela=Tkinter.Tk()
janela.title("Calculator")
largura=235
altura=318
janela.resizable(False,False)
largura_screen=janela.winfo_screenwidth()
altura_screen=janela.winfo_screenheight()
posx=largura_screen/2-largura/2
posy=altura_screen/2-altura/2
janela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
janela.config(bg=cinza)


frame_tela=Tkinter.Frame(janela,width=235,height=50)
frame_tela.grid(row=0,column=0)
janela.mainloop()