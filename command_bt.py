""" Documentacao do Tkinter
http://www.tkdocs.com/tutorial/

"""

from tkinter import *


class Aplication:
    def __init__(self, janela=None):
        """
        Iniciar com um Frame, Um Label, 2 Botoes
        Botao1 = executa o comando
        Botao2 = Sai da aplicação

        """
        # Frame
        self.frame = Frame(janela)
        self.frame.pack()

        # Label
        self.label = Label(self.frame, text="LABEL")
        self.label.pack()

        # Botao Acao
        self.botao = Button(self.frame)
        self.botao.pack()
        self.botao["width"] = 6
        self.botao["text"] = "Acao"
        self.botao.bind("<Button>", self.btAcao)
        self.botao.pack(side=LEFT)

        # Botao Sair
        self.botao = Button(self.frame)
        self.botao.pack()
        self.botao["width"] = 6
        self.botao["text"] = "Sair"
        self.botao["command"] = self.frame.quit
        self.botao.pack(side=LEFT)

    def btAcao(self, event):
        """
        Funcao dada ao Botao1
        Mudara o texto da Label

        """
        if self.label["text"] == "LABEL":
            self.label["text"] = "Its Magic!"
        else:
            self.label["text"] = "LABEL"


root = Tk()

# LARGURA x ALTURA + DISTANCIA.ESQUERDA + DISTANCIA.TOPO
root.geometry("250x70+500+500")

Aplication(root)
root.mainloop()
