import customtkinter as custom
from tkinter import *
from PIL import Image

custom.set_appearance_mode('dark')
custom.set_default_color_theme('dark-blue')

window = custom.CTk()
window.geometry('700x450')
window.title('Ebony SyS')
window.iconbitmap('./Assets/diamante.ico')
window.resizable(False, False)

img = custom.CTkImage(dark_image=Image.open('./Assets/f1.png'), size=(350, 340))

label_img = custom.CTkLabel(master=window, image=img, text='')
label_img.place(x=5, y=65)

title = custom.CTkLabel(master=window, text='👽 Use the FORCE to enter!',
                         text_color='green', font=('Ubuntu Bold', 20))
title.place(x=45, y=5)


frame_texto = custom.CTkFrame(master=window, width=350, height=446)
frame_texto.pack(side=RIGHT)

username = custom.CTkEntry(master=frame_texto, placeholder_text='Nome de usuario',
                           width=300, font=('Ubuntu', 14)).place(x=25, y=150)

username_feedback = custom.CTkLabel(master=frame_texto, text='Este campo é obrigatório ↑',
                                    text_color='green', font=('Ubuntu', 10)).place(x=25, y=178)


password = custom.CTkEntry(master=frame_texto, placeholder_text='Senha',
                           width=300, font=('Ubuntu', 14)).place(x=25, y=210)

password_feedback = custom.CTkLabel(master=frame_texto, text='Este campo é obrigatório ↑',
                                    text_color='green', font=('Ubuntu', 10)).place(x=25, y=238)


window.mainloop()