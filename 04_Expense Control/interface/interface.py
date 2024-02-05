from tkinter import *
from tkinter import Tk, ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# ---------- ROOT ------------ ↓
preto = '#000'
branco = '#fff'
vermelho = '#cc1d4e'
amarelo = '#d1d420'
verde = '#59b356'
cinza = '#d9d9d9'
dark1 = '#101010'
dark2 = '#1e1e1e'
fonte = '#f7f7f5'

cores = ['#5588bb', '#66bbbb',
         '#99bb55', '#ee9944',
         '#444466', '#bb5555'
         ]
# ___________ ROOT ___________ ↑

# --------------- JANELA ----------------- ↓
janela = Tk()
janela.title('Ebony SyS | Despesas')
janela.geometry('900x700')
janela.configure(background=dark2)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
# _______________ JANELA _________________ ↑

# -------------------------------------- FRAME'S -------------------------------------- ↓
frameTopo = Frame(janela, width=1043, height=45, bg=amarelo, relief='flat')
frameTopo.grid(row=0, column=0)

frameGrafico = Frame(janela, width=1043, height=361, bg=dark1, pady=20, relief='raised')
frameGrafico.grid(row=1, column=0, pady=1, padx=10, sticky=NSEW)

frameTabela = Frame(janela, width=1043, height=300, bg=dark1, relief='flat')
frameTabela.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)
# ______________________________________ FRAME'S ______________________________________ ↑


# --------------------------- POSICIONANDO LOGO NO FRAMETOPO -------------------------- ↓
imgLogo = Image.open('../assets/logo_cs_peq.png')
imgLogo = imgLogo.resize((40, 40))
imgLogo = ImageTk.PhotoImage(imgLogo)

labelLogo = Label(frameTopo, image=imgLogo, text='Ebony SyS', width=900, compound=LEFT,
                  padx=5, relief=RAISED, anchor=CENTER, font='Verdana 14 bold italic',
                  bg=dark1, fg=branco, borderwidth=0)
labelLogo.place(x=0, y=0)
# __________________________ POSICIONANDO LOGO NO FRAMETOPO __________________________ ↑


# __________________________ BARRA DE PORCENTAGEM __________________________ ↓

def porcentagem():
    labelPorcentagem = Label(frameGrafico, text='Porcentagem de gastos', height=1, anchor=NW,
                             font=('Verdana 12'), bg=dark1, fg=cinza)
    labelPorcentagem.place(x=40, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('black.Horizonal.TProgressbar', background='#59b356')
    style.configure('TProgressbar', thickness=20)

    barra = Progressbar(frameGrafico, length=188, style='black.Horizontal.TProgressbar')
    barra.place(x=15, y=35)
    barra['value'] = 50

    valor = 50

    labelValor = Label(frameGrafico, text=f'{valor:.1f}%', anchor=NW, font=('Verdana 12'),
                       bg=dark1, fg=cinza)
    labelValor.place(x=210, y=35)


# __________________________ BARRA DE PORCENTAGEM __________________________ ↑
# __________________________ GRÁFICOS __________________________ ↓

def grafico_bar():
    lista_categoria = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [1320, 500, 820]

    # Criando imagem
    figura = plt.Figure(figsize=(4, 3.75), dpi=60, facecolor=dark1)
    ax = figura.add_subplot(111)

    # Inserindo valores para os eixos
    bars = ax.bar(lista_categoria, lista_valores, color=cores, width=0.9)

    # Posicionando valores sobre as barras 
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 3,
                "R${:,.0f}".format(yval),
                ha='center', va='bottom', color='white', fontsize=13, fontstyle='italic')

    # Posicionando as categorias no eixo x
    ax.set_xticklabels(lista_categoria, fontsize=16, color='white')

    # Alterando cores e estilizando gráfico
    ax.patch.set_facecolor(dark1)  # Definindo o fundo do gráfico como preto
    ax.spines['bottom'].set_color(branco)  # Colorindo a linha abaixo das barras
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color(branco)
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color=vermelho)  # linhas da grade
    ax.xaxis.grid(False)

    ax.tick_params(axis='both', colors=branco)

    canva = FigureCanvasTkAgg(figura, frameGrafico)
    canva.get_tk_widget().place(x=10, y=70)


def resumo():
    valor = [500,600,700]

    linha1 = Label(frameGrafico, text='', width=215, height=1, anchor=NW, font=('Ubuntu 1'), bg=branco)
    linha1.place(x=309, y=52)
    sumario1 = Label(frameGrafico, text='Renda Total', anchor=NW, font=('Ubuntu 12'), bg=dark1, fg=branco)
    sumario1.place(x=309, y=35)



porcentagem()
grafico_bar()
resumo()
janela.mainloop()
