import customtkinter as ctk


# general appearance and style settings
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


# colors
light_green= '#014d0d'
dark_green = '#07ed2d'
light_blue = '#63e2ff'
light_red = '#ff3d71'
light_yellow = '#e5f75c'
black = '#000000'
white = '#ffffff'


# create the main window
window = ctk.CTk()
window.geometry('1100x700')
window.iconbitmap('./src/icon/diamante.ico')
window.title('Lista de Tarefas - Leonardo Alves')
window.resizable(False, False)


frame_top = ctk.CTkFrame(window, width=1080, height=40)
frame_top.place(x=10, y=10)






window.mainloop()
