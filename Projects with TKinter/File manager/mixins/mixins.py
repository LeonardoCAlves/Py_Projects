import os
import shutil

from views import *

# root cores
preto = '#000'
branco = '#fff'
dark1 = '#3F3F3F'
dark2 = '#1f1f1f'

amarelo = '#ffff00'
azul_claro = '#836fff'
azul_escuro = '#000080'
verde_claro = '#00ff00'
verde_escuro = '#228d22'
vermelho = '#ff0000'
violeta = '#9400f3'
rosa = '#ff00ff'
laranja = '#ff8c00'

cores = [
    amarelo, azul_claro, azul_escuro,
    verde_claro, verde_escuro, vermelho,
    violeta, rosa, laranja
]

# root fonte
fonte_principal = 'Ubuntu 16 bold'
cor_fonte_principal = '#f0f8ff'
fonte_secundaria = 'Ubuntu 12'
cor_fonte_secundaria = '#ffd700'

# root imagens
img_logo = '../assets/img/logo.png'
icone_pasta = '../assets/img/pasta.png'
icone_copiar = '../assets/img/copiar.png'
icone_mover = '../assets/img/mover.png'
icone_deletar = '../assets/img/deletar.png'

# função para contar pastas
def contarPastasArquivos(caminho, extensao):
    qtd_pastas = 0
    qtd_arquivos = 0

    for item in os.listdir(caminho):
        if os.path.isfile(os.path.join(caminho, item)) and item.endswith(extensao):
            qtd_arquivos += 1

        if os.path.isdir(os.path.join(caminho, item)):
            qtd_pastas += 1
            subpasta_path = os.path.join(caminho, item)
            qtd_subarquivos, qtd_subpastas = contarPastasArquivos(subpasta_path, extensao)
            qtd_pastas += qtd_subpastas
            qtd_arquivos += qtd_subarquivos

    return qtd_pastas, qtd_arquivos


# copiando arquivos
def copiarArquivos(origem, destino, ext):

    origem = origem
    destino = destino
    extensao = ext

    for nome in os.listdir(origem):
        if nome.endswith(extensao):
            caminho_origem = os.path.join(origem, nome)
            caminho_destino = os.path.join(destino, nome)
            shutil.copy(caminho_origem, caminho_destino)


def moverArquivos(origem, destino, ext):

    origem = origem
    destino = destino
    extensao = ext

    for nome in os.listdir(origem):
        if nome.endswith(extensao):
            caminho_origem = os.path.join(origem, nome)
            caminho_destino = os.path.join(destino, nome)
            shutil.move(caminho_origem, caminho_destino)