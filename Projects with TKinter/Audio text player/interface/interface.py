import PySimpleGUI as sg
import os
from inspect import Traceback
from gtts import gTTS, lang
from playsound import playsound

def Speaking(text):
    textSpeaking = gTTS(text=text, lang='pt-br', slow=False)
    filename = 'audio.mp3'
    textSpeaking.save(filename)
    playsound(filename)
    os.remove(filename)


def initWindow():
    sg.theme('Dark')
    fileTypes = [("Todos arquivos", "*.*")]
    layout = [[sg.Text('Vamos lá, escolha um arquivo!')],
              [sg.Text(size=(30, 1), key='fileSelected')],
              [sg.Input(size=(30, 1), key="-FILE-"),
               sg.FileBrowse(file_types=fileTypes, key='file_browse'),
               sg.Button('Ler arquivo', key='fileReading')]]

    return sg.Window('@ebony.programador | Códigos Simples', layout=layout, finalize=True, element_justification='c')


windowOne = initWindow()

while True:
    window, event, values = sg.read_all_windows()
    if window == windowOne and event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if window == windowOne and event == 'fileReading':
        filePath = values['-FILE-']
        fileName = os.path.basename(filePath)
        window['fileSelected'].update(f'lido → {fileName}', text_color='white')
        try:
            if fileName[-4:] == '.txt':
                with open(filePath) as text_to_read:
                    txt = text_to_read.read()
                    Speaking(txt)
            else:
                window['fileSelected'].update('Ops, ainda não suporto este arquivo!', text_color='red')
        except:
            window['fileSelected'].update('Ops, este arquivo está vazio!', text_color='red')
        if filePath == '':
            window['fileSelected'].update('Hey, selecione um arquivo!', text_color='red')
window.close()

