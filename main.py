import pyautogui as spam
import time
from tkinter import *



def execucao():
    i=0

    time.sleep(2)
    msg1 = int(msg.get())
    ed1 = str(ed.get())
    while i <= int(msg1):
        spam.typewrite(f"{i}. {ed1}")
        spam.press("Enter")
        i+=1

window = Tk()
window.title("Loop de mensagens")

ed = Entry(window)
ed.grid(column=1, row=0)

msg = Entry(window)
msg.grid(column=1, row=2)


text_intro = Label(window, text="ATENÇÃO: APÓS CLICAR EM INICIAR, CLIQUE RAPIDAMENTE NA CAIXA DE TEXTO ONDE" "\n DESEJA ENVIAR A MENSAGEM",)
text_intro.place(x=50, y=350)

text_msg = Label(window, text="Qual mensagem devo enviar? ", padx=100, pady=70)
text_msg.grid(column=0, row=0)

text_msg = Label(window, text="Numero de mensagens: ")
text_msg.grid(column=0, row=2)

botao = Button(window, text="Iniciar", command=execucao, padx=50 , pady=15)
botao.place(x=230, y=250)


window.geometry("600x500")
window.mainloop()


