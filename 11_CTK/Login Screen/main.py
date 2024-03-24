import customtkinter as custom
from tkinter import *

custom.set_appearance_mode('dark')
custom.set_default_color_theme('dark-blue')

window = custom.CTk()
window.geometry('700x450')
window.title('Ebony SyS')
window.iconbitmap('./Assets/diamante.ico')
window.resizable(False, False)

img = PhotoImage(file='./Assets/f1.png')
label_img = custom.CTkLabel(master=window, image=img, text='')
label_img.place(x=5, y=65)

frame_texto = custom.CTkFrame(master=window, width=350, height=446)
frame_texto.pack(side=RIGHT)

title = custom.CTkLabel(master=frame_texto, text='Use the FORCE to enter!',
                         text_color='green', font=('Ubuntu Bold', 25))
title.place(x=40, y=5)

username = custom.CTkEntry(master=frame_texto, placeholder_text='Nome de usuario',
                           width=300, font=('Ubuntu', 14)).place(x=25, y=100)

username_feedback = custom.CTkLabel(master=frame_texto, text='Este campo é obrigatório ↑',
                                    text_color='green', font=('Ubuntu', 10)).place(x=25, y=128)


password = custom.CTkEntry(master=frame_texto, placeholder_text='Senha',
                           width=300, font=('Ubuntu', 14)).place(x=25, y=180)

password_feedback = custom.CTkLabel(master=frame_texto, text='Este campo é obrigatório ↑',
                                    text_color='green', font=('Ubuntu', 10)).place(x=25, y=208)


window.mainloop()