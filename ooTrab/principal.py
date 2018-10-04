from ooTrab.Juros import *
import tkinter as tk
from tkinter import *

def calcular():
    if vInicial.get() == "" or vInicial.get() == " ":
        montanteA = float(montante.get())
        periodoA = float(periodo.get())
        taxaA = float(taxa.get())
        jurosA = Juros(0, taxaA, periodoA, montanteA)

    if taxa.get() == "" or taxa.get() == " ":
        montanteA = float(montante.get())
        periodoA = float(periodo.get())
        valorInicial = float(vInicial.get())
        jurosA = Juros(valorInicial, 0, periodoA, montanteA)

    if periodo.get() == "" or periodo.get() == " ":
        montanteA = float(montante.get())
        taxaA = float(taxa.get())
        valorInicial = float(vInicial.get())
        jurosA = Juros(valorInicial, taxaA, 0, montanteA)


    if montante.get() == "" or montante.get() == " ":
        periodoA = float(periodo.get())
        taxaA = float(taxa.get())
        valorInicial = float(vInicial.get())
        jurosA = Juros(valorInicial, taxaA, periodoA, 0)

    tipo = v.get()
    if tipo == "simples":
        if montante.get() == "" or montante.get() ==" ":
            jurosA = Juros.jurosSimplesMontante(jurosA)
            montante.delete(0,END)
            montante.insert(0, jurosA.montante)

        if vInicial.get() == "" or vInicial.get() == " ":
            jurosA = Juros.jurosSimplesVinicial(jurosA)
            vInicial.delete(0, END)
            vInicial.insert(0, jurosA.vInicial)

        if taxa.get() == "" or taxa.get() == " ":
            jurosA = Juros.jurosSimplesTaxa(jurosA)
            taxa.delete(0, END)
            taxa.insert(0, jurosA.taxa)

        if periodo.get() == "" or periodo.get() == " ":
            jurosA = Juros.jurosSimplesPeriodo(jurosA)
            periodo.delete(0, END)
            periodo.insert(0, jurosA.tempo)

    if tipo == "composto":
        if montante.get() == "" or montante.get() == " ":
            jurosA = Juros.jurosCompostosMontante(jurosA)
            montante.delete(0, END)
            montante.insert(0, jurosA.montante)

        if vInicial.get() == "" or vInicial.get() == " ":
            jurosA = Juros.jurosCompostosVinicial(jurosA)
            vInicial.delete(0, END)
            vInicial.insert(0, jurosA.vInicial)

        if taxa.get() == "" or taxa.get() == " ":
            jurosA = Juros.jurosCompostosTaxa(jurosA)
            taxa.delete(0, END)
            taxa.insert(0, jurosA.taxa)

        if periodo.get() == "" or periodo.get() == " ":
            jurosA = Juros.jurosCompostosPerioso(jurosA)
            periodo.delete(0, END)
            periodo.insert(0, jurosA.tempo)

janela1 = tk.Tk()
janela1.title("SIMULAÇÃO DE JUROS")
janela1["bg"] = "white"
janela1.geometry("260x300")

v = StringVar()
simples = Radiobutton(janela1, text="JUROS SIMPLES", value="simples", bg="white", variable=v)
simples.place(x=10, y=270)
v.set("simples")

compostos = Radiobutton(janela1, text="JUROS COMPOSTOS", value="composto", bg="white", variable=v)
compostos.place(x=120, y=270)

tx = Label(janela1, text="Capital Inicial:", font=("Arial", 10), bg="white")
tx.place(x=8, y=10)
vInicial = Entry(janela1, width=40)
vInicial.place(x=7, y=30)

tx2 = Label(janela1, text="Taxa de Juros ao Mês:", font=("Arial", 10), bg="white")
tx2.place(x=8, y=70)
taxa = Entry(janela1, width=40)
taxa.place(x=7, y=90)

tx3 = Label(janela1, text="Periodos em Meses:", font=("Arial", 10), bg="white")
tx3.place(x=8, y=130)
periodo = Entry(janela1, width=40)
periodo.place(x=7, y=150)

btCalc = Button(janela1, width=10, text="Calcular", bg="white", command=calcular)
btCalc.place(x=90, y=240)

tx4 = Label(janela1, text="Montante: ", font=("Arial", 10), bg="white")
tx4.place(x=8, y=180)

montante = Entry(janela1, width=40)
montante.place(x=7, y=200)

janela1.mainloop()