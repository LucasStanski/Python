import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
#Criação e possicionamento central da jenala
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
janela=ctk.CTk()
janela.title("Curso Tkinter")
largura=700
altura=500
largura_screen=janela.winfo_screenwidth()
altura_screen=janela.winfo_screenheight()
posx=largura_screen/2-largura/2
posy=altura_screen/2-altura/2
janela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))

ka=ctk.CTkEntry(janela, placeholder_text="Informacao").place(x=50,y=430)

janela.mainloop()
