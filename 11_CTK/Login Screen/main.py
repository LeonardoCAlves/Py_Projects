import customtkinter as custom
from tkinter import *
from PIL import Image

# general appearance and style settings
custom.set_appearance_mode('dark')
custom.set_default_color_theme('dark-blue')


# creating the main window
window = custom.CTk()
window.geometry('700x450')
window.title('Ebony SyS')
window.iconbitmap('./Assets/diamante.ico')
window.resizable(False, False)


# text above the image
title = custom.CTkLabel(master=window, text='👽 Use the FORCE to enter!',
                         text_color='green', font=('Ubuntu Bold', 20))
title.place(x=45, y=5)


# importing the image that will be on the screen
img = custom.CTkImage(dark_image=Image.open('./Assets/f1.png'), size=(350, 340))
label_img = custom.CTkLabel(master=window, image=img, text='')
label_img.place(x=5, y=65)


# creating the frame where the inputs will be
frame_texto = custom.CTkFrame(master=window, width=350, height=446)
frame_texto.pack(side=RIGHT)


# Username
username = custom.CTkEntry(master=frame_texto, placeholder_text='Nome de usuario',
                           width=300, font=('Ubuntu', 14)).place(x=25, y=120)
username_feedback = custom.CTkLabel(master=frame_texto, text='Este campo é obrigatório ↑',
                                    text_color='green', font=('Ubuntu', 10)).place(x=25, y=148)


# Password
password = custom.CTkEntry(master=frame_texto, placeholder_text='Senha', show='👽',
                           width=300, font=('Ubuntu', 14)).place(x=25, y=180)
password_feedback = custom.CTkLabel(master=frame_texto, text='Este campo é obrigatório ↑',
                                    text_color='green', font=('Ubuntu', 10)).place(x=25, y=208)


# checkbox to keep user and password data
checkbox = custom.CTkCheckBox(master=frame_texto, text="Continuar conectado...",
                              checkbox_width=12, checkbox_height=12, 
                              border_width=2, border_color='#00ff00',
                              hover_color='#00ffff').place(x=25, y=240)


# enter button
btn_entrar = custom.CTkButton(master=frame_texto, 
                              width=100, 
                              text='Entrar', 
                              text_color='#00ff00').place(x=120, y=280)


window.mainloop()