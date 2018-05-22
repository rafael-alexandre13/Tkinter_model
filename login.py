""" Tela de Login """

from tkinter import *


class Application:
    def __init__(self, master=None):
        """
        Inicia uma janela com
        Frame1 [Titulo]
        Frame2 [Label Nome, Caixa de entrada]
        Frame3 [Label Senha, Caixa de entrada]
        Frame4 [Botao, Label Confirmacao]

        """

        # Frame1 Inicio
        self.frame1 = Frame(master)
        self.frame1["pady"] = 10
        self.frame1.pack()

        self.title = Label(self.frame1, text="Login")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()
        # Frame1 Fim

        # Frame2 Inicio
        self.frame2 = Frame(master)
        self.frame2["padx"] = 20
        self.frame2.pack()

        self.nomeLabel = Label(self.frame2, text="{:<5}".format("Nome"))
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.frame2)
        self.nome["width"] = 30
        self.nome.pack(side=LEFT)
        # Frame2 Fim

        # Frame3 Inicio
        self.frame3 = Frame(master)
        self.frame3["padx"] = 20
        self.frame3.pack()

        self.labelSenha = Label(self.frame3, text="Senha")
        self.labelSenha.pack(side=LEFT)

        self.senha = Entry(self.frame3)
        self.senha["width"] = 30
        self.senha["show"] = "*"
        self.senha.bind("<Return>", self.verificaSenha)
        self.senha.pack(side=LEFT)
        # Frame2 Fim

        # Frame3 Inicio
        self.frame4 = Frame(master)
        self.frame4["pady"] = 20
        self.frame4.pack()

        self.autent = Button(self.frame4)
        self.autent["text"] = "Autenticar"
        self.autent["width"] = 12
        self.autent.bind("<Button>", self.verificaSenha)
        self.autent.pack()

        self.labelMensagem = Label(self.frame4, text="")
        self.labelMensagem.pack()
        # Frame2 Fim

    # Funcoes
    def verificaSenha(self, event):
        """
        Método verificar senha

        """
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "rafael" and senha == "1234":
            self.labelMensagem["text"] = "Autenticado"
        else:
            self.labelMensagem["text"] = "Erro na autenticação"


root = Tk()
Application(root)
root.mainloop()