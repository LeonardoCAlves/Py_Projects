from tkinter import *
from tkinter import Tk, StringVar
from tkinter import ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mixins.mixins
from mixins import *
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
import shutil

# --------------------- criando janela
janela = Tk()
janela.geometry('1080x700')
janela.title('Ebony SyS')
janela.resizable(width=FALSE, height=FALSE)
logo = PhotoImage(file=mixins.img_logo)
janela.iconphoto(False, logo)
style = ttk.Style(janela)
style.theme_use("clam")

# --------------------- frame header
frame_header = Frame(janela, width=1080, height=35, bg=mixins.dark2, relief='flat')
frame_header.grid(row=0, column=0)

icone_pasta = Image.open(mixins.icone_pasta)
icone_pasta = icone_pasta.resize((30, 30))
icone_pasta = ImageTk.PhotoImage(icone_pasta)

iconePasta = Label(frame_header, image=icone_pasta,
                   text='Gerenciador de Arquivos', width=1080, compound=LEFT,
                   padx=5, relief=RAISED, anchor=CENTER, font=mixins.fonte_principal,
                   bg=mixins.dark2, fg=mixins.cor_fonte_principal, borderwidth=0)
iconePasta.place(x=0, y=0)

# --------------------- frame main
frame_main = Frame(janela, width=1080, height=635, bg=mixins.dark1)
frame_main.grid(row=1, column=0, sticky=NSEW)

# --------------------- frame main/grafico
frame_grafico = Frame(frame_main, width=680, height=655, bg=mixins.dark1, pady=50)
frame_grafico.place(x=351, y=0)

global pasta


# funcão para renderizar o gráfico
def grafico(x, y):
    figura = plt.Figure(figsize=(4.7, 4), dpi=130)
    figura.set_facecolor(mixins.dark1)
    ax = figura.add_subplot(111)

    qtd = x
    ext = y

    ax.pie(qtd, wedgeprops=dict(width=.4), colors=mixins.cores,
           shadow=True, startangle=90, labeldistance=2)
    ax.legend(ext, loc='center right', bbox_to_anchor=(1.25, .5),
              fontsize='small', title='Extensões', facecolor=mixins.dark1)

    canva = FigureCanvasTkAgg(figura, frame_grafico)
    canva.get_tk_widget().grid(row=0, column=0, sticky=NSEW)


# função para escolher uma pasta
def escolherPasta():
    global pasta
    pasta = fd.askdirectory()

    extensoes = ['.txt', '.csv', '.xlsx', '.pdf', '.json', '.jpg', '.jpeg', '.png',
                 '.mp3', '.mp4', '.avi', '.html', '.css', '.sass', '.js', '.py',
                 '.sql', '.ty']

    extensoes_combobox = []
    extensoes_encontradas = []
    extensoes_quantidade = []
    quantidade_pastas = 0

    for item in extensoes:
        caminho = pasta
        extensao = item
        qtd_arquivos, qtd_pastas = mixins.contarPastasArquivos(caminho, extensao)

        if qtd_arquivos <= 0:
            pass
        else:
            extensoes_encontradas.append(f'{item}: {str(qtd_arquivos)}')
            extensoes_combobox.append(item)
            extensoes_quantidade.append(qtd_arquivos)
            quantidade_pastas = qtd_pastas




    extensoes_encontradas.append(f'Pastas: {str(quantidade_pastas)}')
    extensoes_quantidade.append(quantidade_pastas)

    box_extensao['values'] = extensoes_combobox
    box_extensao_mover['values'] = extensoes_combobox
    box_extensao_deletar['values'] = extensoes_combobox

    grafico(extensoes_quantidade, extensoes_encontradas)


# --------------------- frame main/entrada
frame_entrada = Frame(frame_main, width=400, height=655, bg=mixins.dark2)
frame_entrada.place(x=0, y=0)
frame_entrada.lift()


def copiar():
    global pasta

    if len(box_extensao.get()) == 0:
        messagebox.showerror('Ops :(', 'Escolha um ficheiro primeiro.')
    else:
        extensao = box_extensao.get()
        destino = fd.askdirectory()
        mixins.copiarArquivos(pasta, destino, extensao)
        messagebox.showinfo('Copiar', 'Arquivos copiados com sucesso!')
        box_extensao.delete(0, END)


def mover():
    global pasta

    if len(box_extensao_mover.get()) == 0:
        messagebox.showerror(':(', 'Escolha um ficheiro primeiro.')
    else:
        extensao = box_extensao_mover.get()
        destino = fd.askdirectory()
        mixins.moverArquivos(pasta, destino, extensao)
        messagebox.showinfo(':)', 'Arquivos movidos com sucesso!')
        box_extensao_mover.delete(0, END)


def deletar():
    ...


# --------------------- ESCOLHER PASTA
label_escolher_pasta = Label(frame_entrada, text='Escolha uma pasta',
                             anchor=CENTER, relief='flat',
                             bg=mixins.dark2, fg=mixins.cor_fonte_principal,
                             font=mixins.fonte_secundaria)
label_escolher_pasta.place(x=145, y=30)

btn_escolher = Button(frame_entrada, command=escolherPasta, text='Escolher',
                      width=15, overrelief=RIDGE, bg=mixins.dark2,
                      fg=mixins.cor_fonte_principal)
btn_escolher.place(x=155, y=65)

# --------------------- COPIAR ARQUIVOS
label_copiar = Label(frame_entrada, text="Copiar Arquivos", anchor=CENTER, bg=mixins.dark2,
                     fg=mixins.cor_fonte_principal, font=mixins.fonte_secundaria,
                     relief='flat')
label_copiar.place(x=10, y=120)

box_extensao = ttk.Combobox(frame_entrada, width=8, font=mixins.fonte_secundaria)
box_extensao.place(x=135, y=120, relheight=0.04)

iconeCopiar = Image.open(mixins.icone_copiar)
iconeCopiar = iconeCopiar.resize((17, 17))
iconeCopiar = ImageTk.PhotoImage(iconeCopiar)

btn_copiar = Button(frame_entrada, text='Escolher destino', command=copiar, image=iconeCopiar,
                    width=150, overrelief=RIDGE, bg=mixins.dark2, compound=LEFT,
                    fg=mixins.cor_fonte_principal, font=mixins.fonte_secundaria,
                    padx=2)
btn_copiar.place(x=235, y=120, relheight=0.04)

# --------------------- MOVER ARQUIVOS
label_mover = Label(frame_entrada, text="Mover Arquivos", anchor=CENTER, bg=mixins.dark2,
                    fg=mixins.cor_fonte_principal, font=mixins.fonte_secundaria,
                    relief='flat')
label_mover.place(x=10, y=170)

box_extensao_mover = ttk.Combobox(frame_entrada, width=8, font=mixins.fonte_secundaria)
box_extensao_mover.place(x=135, y=170, relheight=0.04)

iconeMover = Image.open(mixins.icone_mover)
iconeMover = iconeMover.resize((17, 17))
iconeMover = ImageTk.PhotoImage(iconeMover)

btn_mover = Button(frame_entrada, text='Escolher destino', command=mover, image=iconeMover,
                   width=150, overrelief=RIDGE, bg=mixins.dark2, compound=LEFT,
                   fg=mixins.cor_fonte_principal, font=mixins.fonte_secundaria,
                   padx=2)
btn_mover.place(x=235, y=170, relheight=0.04)

# --------------------- DELETAR ARQUIVOS
label_deletar = Label(frame_entrada, text="Deletar Arquivos", anchor=CENTER, bg=mixins.dark2,
                    fg=mixins.cor_fonte_principal, font=mixins.fonte_secundaria,
                    relief='flat')
label_deletar.place(x=10, y=220)

box_extensao_deletar = ttk.Combobox(frame_entrada, width=8, font=mixins.fonte_secundaria)
box_extensao_deletar.place(x=135, y=220, relheight=0.04)

iconeDeletar = Image.open(mixins.icone_deletar)
iconeDeletar = iconeDeletar.resize((17, 17))
iconeDeletar = ImageTk.PhotoImage(iconeDeletar)

btn_deletar = Button(frame_entrada, text='Deletar Arquivo', command=deletar,
                     image=iconeDeletar, width=150, overrelief=RIDGE, bg=mixins.dark2,
                     compound=LEFT, fg=mixins.cor_fonte_principal,
                     font=mixins.fonte_secundaria, padx=2)
btn_deletar.place(x=235, y=220, relheight=0.04)


# --------------------- frame footer
frame_footer = Frame(janela, width=1080, height=30, bg=mixins.dark1)
frame_footer.grid(row=3, column=0)

icone_logo = Image.open(mixins.img_logo)
icone_logo = icone_logo.resize((15, 15))
icone_logo = ImageTk.PhotoImage(icone_logo)

label_footer = Label(frame_footer, image=icone_logo,
                   text=f'Ebony SyS', width=1080, compound=CENTER,
                   padx=5, relief=RAISED, anchor=CENTER, font=mixins.fonte_secundaria,
                   bg=mixins.dark2, fg=mixins.cor_fonte_secundaria, borderwidth=0)
label_footer.grid(row=0, column=0)
janela.mainloop()
