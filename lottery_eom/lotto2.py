from tkinter import *
from random import shuffle


# initializing a new window
def lotto2():
    root = Tk()
    root.geometry("300x300")
    root.title("Ithuba National Lottery")

    def win():
        lottery = list(range(1, 60))
        numbers = []

        for i in range(6):
            shuffle(lottery)
            x = lottery.pop()
            numbers.append(x)

            numbers.sort()
            print(numbers)

        btn = Button(root, text="yyh6", command=win)
        btn.pack()

        root.mainloop()
