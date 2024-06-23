from tkinter import *
from tkinter import Tk, ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from ttkthemes import ThemedStyle
from tkcalendar import Calendar, DateEntry
from datetime import date
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

frameInferior = Frame(janela, width=1043, height=300, bg=dark1, relief='flat')
frameInferior.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

frameGraficoPie = Frame(frameGrafico, width=580, height=250, bg=dark1)
frameGraficoPie.place(x=415, y=20)

frameRenda = Frame(frameInferior, width=300, height=250, bg=dark1)
frameRenda.grid(row=0, column=0)

frameAddRemDespesas = Frame(frameInferior, width=220, height=250, bg=dark1)
frameAddRemDespesas.grid(row=0, column=1, padx=5)

frameAddRemReceitas = Frame(frameInferior, width=220, height=250, bg=dark1)
frameAddRemReceitas.grid(row=0, column=2, padx=5)
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


def barra_porcentagem():
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
    ax.yaxis.grid(False, color=cinza)  # linhas da grade
    ax.xaxis.grid(False)

    ax.tick_params(axis='both', colors=branco)

    canva = FigureCanvasTkAgg(figura, frameGrafico)
    canva.get_tk_widget().place(x=10, y=70)

def resumo():
    valor = [500,600,700]

    linha = Label(frameGrafico, text='', width=215, height=1, anchor=NW, font=('Ubuntu 1'), bg=branco)
    linha.place(x=309, y=47)
    sumario = Label(frameGrafico, text='Renda Total'.center(44), anchor=NW, font=('Ubuntu 12'), bg=dark1, fg=branco)
    sumario.place(x=309, y=50)
    sumario = Label(frameGrafico, text=f'R$ {valor[0]:,.2f}', anchor=NW, font=('Ubuntu 15'), bg=dark1, fg=branco)
    sumario.place(x=309, y=80)

    linha = Label(frameGrafico, text='', width=215, height=1, anchor=NW, font=('Ubuntu 1'), bg=branco)
    linha.place(x=309, y=137)
    sumario = Label(frameGrafico, text='Despesa Total'.center(44), anchor=NW, font=('Ubuntu 12'), bg=dark1, fg=branco)
    sumario.place(x=309, y=140)
    sumario = Label(frameGrafico, text=f'R$ {valor[0]:,.2f}', anchor=NW, font=('Ubuntu 15'), bg=dark1, fg=branco)
    sumario.place(x=309, y=170)

    linha = Label(frameGrafico, text='', width=215, height=1, anchor=NW, font=('Ubuntu 1'), bg=branco)
    linha.place(x=309, y=227)
    sumario = Label(frameGrafico, text='Saldo Total'.center(45), anchor=NW, font=('Ubuntu 12'), bg=dark1, fg=branco)
    sumario.place(x=309, y=230)
    sumario = Label(frameGrafico, text=f'R$ {valor[0]:,.2f}', anchor=NW, font=('Ubuntu 15'), bg=dark1, fg=branco)
    sumario.place(x=309, y=260)

def grafico_pie():
    # criando a figura
    figura = plt.Figure(figsize=(5,3), dpi=90, facecolor=dark1)
    ax = figura.add_subplot(111)

    lista_valores = [345, 218, 539]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    cor_fonte = {'color': branco}

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=cores,
           shadow=True, startangle=90, textprops=cor_fonte, labeldistance=1.)

    # Configurando a legenda
    legenda = ax.legend(lista_categorias, loc='center right', bbox_to_anchor=(1.55, 0.50), facecolor=dark1)

    # Configurando a cor de fundo da legenda
    legenda.set_frame_on(True)
    legenda.get_frame().set_facecolor(dark1)

    # Configurando a cor da fonte na legenda
    for texto in legenda.get_texts():
        texto.set_color(branco)

    canva_categoria = FigureCanvasTkAgg(figura, frameGraficoPie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


# Tabela de renda mensal
app_tabela = Label(frameGrafico, text="Tabela Receitas Vs Despesas", anchor=NW,
                   font=("Ubuntu 12"), bg=dark1, fg=branco)
app_tabela.place(x=60, y=312)

def tabela():
    cabecalho = ['ID', 'Categoria', 'Data', 'Valor']
    lista_itens = [
                    [1,'Despesa','14/02/2024', 'R$4.550,00'],
                    [2,'Despesa','10/02/2024', 'R$1.200,00'],
                    [3,'Despesa','08/02/2024', 'R$3.780,00'],
                    [4,'Despesa','02/02/2024', 'R$3.230,00']
                  ]

    global tree

    style = ThemedStyle()
    style.set_theme("black")
    style.configure(
        "Treeview",
        background=dark1,
        foreground=branco,
        fieldbackground=dark1,
        font=("Ubuntu", 9),
        rowheight=25)  

    style.configure(
        "Treeview.Heading", 
        background=dark2, 
        foreground=branco, 
        borderwidth=0, 
        font=("Ubuntu", 13))
    
    tree = ttk.Treeview(
        frameRenda, 
        style="Treeview", 
        selectmode='extended', 
        columns=cabecalho, 
        show='headings')
    
    scrollbar_vert = ttk.Scrollbar(
        frameRenda, 
        orient='vertical', 
        command=tree.yview, 
        style="Vertical.TScrollbar")
    
    scrollbar_hori = ttk.Scrollbar(
        frameRenda, 
        orient='horizontal', 
        command=tree.xview, 
        style="Horizontal.TScrollbar")
    
    tree.configure(
        yscrollcommand=scrollbar_vert.set, 
        xscrollcommand=scrollbar_hori.set
    )

    tree.grid(column=0, row=0, sticky='nsew')
    scrollbar_vert.grid(column=1, row=0, sticky='ns')
    scrollbar_hori.grid(column=0, row=1, sticky='ew')

    hd = ['center','center','center','center']
    h = [30, 100, 100, 100]
    n = 0

    for col in cabecalho:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


label_descricao = Label(frameGrafico, text='Novas despesas', height=1,
                        anchor=NW, bg=dark1, font=('Ubuntu 12'), fg=branco)
label_descricao.place(x=390, y=312)

# Linha de categorias 
label_categoria = Label(frameAddRemDespesas, text='Categorias', height=1,
                        anchor=NW, bg=dark1, font=('Ubuntu 12'), fg=branco)
label_categoria.place(x=10, y=10)

# Carregando as categorias
lista_categorias = ['Viagem', 'Comida']
categorias = []

for c in lista_categorias : categorias.append(c[1])

combo_categoriaDespesa = ttk.Combobox(frameAddRemDespesas, width=10, font=('Ivy 10'))
combo_categoriaDespesa['values'] = (categorias)
combo_categoriaDespesa.place(x=110, y=11)


# Linha da data despesa
label_despesa = Label(frameAddRemDespesas, text='Data', height=1,
                        anchor=NW, bg=dark1, font=('Ubuntu 12'), fg=branco)
label_despesa.place(x=10, y=50)

cal_despesa = DateEntry(frameAddRemDespesas, width=12, background='darkblue',
                        foreground='white', borderwidth=2, year=2024, justify='center')
cal_despesa.place(x=110, y=51)


# Linha do valor
label_valor = Label(frameAddRemDespesas, text='Valor R$', height=1,
                        anchor=NW, bg=dark1, font=('Ubuntu 12'), fg=branco)
label_valor.place(x=10, y=90)
cal_valor = Entry(frameAddRemDespesas, width=15, justify='left', relief='solid')
cal_valor.place(x=110, y=91)


# Botão adicionar despesa
btn_adc_despesa = Button(frameAddRemDespesas, text='Adicionar', bg=verde, fg=branco, width=12,
                         compound=LEFT, font=('Ivy 7 bold'), overrelief=RIDGE)
btn_adc_despesa.place(x=10, y=141)


# Botão remover despesa
btn_del_despesa = Button(frameAddRemDespesas, text='Remover', bg=vermelho, fg=branco, width=12, 
                         compound=LEFT, font=('Ivy 7 bold'), overrelief=RIDGE)
btn_del_despesa.place(x=124, y=141)

# label Novas Receitas
label_descricao = Label(frameGrafico, text='Novas receitas', height=1,
                        anchor=NW, bg=dark1, font=('Ubuntu 12'), fg=branco)
label_descricao.place(x=690, y=312)


# Linha da data receita
label_despesa = Label(frameAddRemReceitas, text='Data', height=1,
                        anchor=NW, bg=dark1, font=('Ubuntu 12'), fg=branco)
label_despesa.place(x=20, y=10)

cal_despesa = DateEntry(frameAddRemReceitas, width=12, background='darkblue',
                        foreground='white', borderwidth=2, year=2024, justify='center')
cal_despesa.place(x=70, y=11)











barra_porcentagem()
grafico_bar()
resumo()
grafico_pie()
tabela()
janela.mainloop()
