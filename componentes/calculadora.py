from tkinter.messagebox import showerror
from tkinter import *


class CalculatorApp:
    def __init__(self):
        self.__root = Tk()

        #  Configurações de tamanho de tela
        self.__root.geometry('210x260+500+500')
        self.__root.resizable(0, 0)
        self.__root.configure(bg='#2b2b2b')
        self.__root.title("Calculadora")


        # Visor
        self.__visor = Entry(
            self.__root,
            width=16,
            font=('arial', 16, 'bold'),
            fg='#c8c8c8',
            relief='flat',
            bd=0,
            bg="#333333"
        )

        # Botões
        self.__keyboard = Frame(self.__root)

        but0 = Button(
            self.__keyboard,
            text='0',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '0')
        )

        but1 = Button(
            self.__keyboard,
            text='1',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '1')
        )

        but2 = Button(
            self.__keyboard,
            text='2',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '2')
        )

        but3 = Button(
            self.__keyboard,
            text='3',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '3')
        )

        but4 = Button(
            self.__keyboard,
            text='4',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '4')
        )

        but5 = Button(
            self.__keyboard,
            text='5',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '5')
        )

        but6 = Button(
            self.__keyboard,
            text='6',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END,'6')
        )

        but7 = Button(
            self.__keyboard,
            text='7',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '7')
        )

        but8 = Button(
            self.__keyboard,
            text='8',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '8')
        )

        but9 = Button(
            self.__keyboard,
            text='9',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '9')
        )

        but_soma = Button(
            self.__keyboard,
            text='+',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '+')
        )

        but_sub = Button(
            self.__keyboard,
            text='-',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '-')
        )

        but_div = Button(
            self.__keyboard,
            text='/',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '/')
        )

        but_mult = Button(
            self.__keyboard,
            text='*',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '*')
        )

        but_ponto = Button(
            self.__keyboard,
            text='.',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=lambda: self.__visor.insert(END, '.')
        )

        but_resu = Button(
            self.__keyboard,
            text='=',
            width=6,
            height=3,
            relief='flat',
            bg='#333333',
            fg='#c8c8c8',
            bd=0,
            command=self.calcular
        )

        #  Posicionamento

        but0.grid(row=4, column=1)
        but1.grid(row=3, column=0)
        but2.grid(row=3, column=1)
        but3.grid(row=3, column=2)
        but4.grid(row=2, column=0)
        but5.grid(row=2, column=1)
        but6.grid(row=2, column=2)
        but7.grid(row=1, column=0)
        but8.grid(row=1, column=1)
        but9.grid(row=1, column=2)
        but_soma.grid(row=4, column=3)
        but_sub.grid(row=3, column=3)
        but_div.grid(row=2, column=3)
        but_mult.grid(row=1, column=3)
        but_ponto.grid(row=4, column=0)
        but_resu.grid(row=4, column=2)

        self.__visor.place(x=7, y=10)
        self.__keyboard.place(x=9, y=45)
        self.__root.mainloop()


    def calcular(self):
        resul: str = self.__visor.get()
        try:
            for char in resul:
                if not (char.isnumeric() or char in ['.', '+', '-', '*', '/']):
                    raise ValueError("Operação inválida")
            self.__visor.delete(0, END)
            self.__visor.insert(0, f"{str(round(eval(resul), 3))}")
        except ArithmeticError:
            showerror("Operação inválida", f"Operação inválida expressão '{resul}' desonhecida")

        except ValueError:
            showerror("caractere desconhecido", f"'{resul}' não pode ser reconhecida como uma expressão matematica")
        except Exception as excp:
           print(excp)
