from tkinter import *
from tkinter import messagebox
from random import shuffle
from datetime import *

# initializing a window
window = Tk()
window.geometry("300x300")
window.configure(bg='yellow')

#date and time
date = datetime.now()
date_label = Label(window)
date_label.pack()
date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))


# button functions
def verify():
    try:
        age = entry1.get()
        if int(entry1.get()) >= 18:
            window.destroy()
            run = Lotto()

        else:
            messagebox.showinfo("Verify", "Sorry , you are too young to play")
    except ValueError:
        messagebox.showinfo("error", "Please enter a valid number")


# initializing a new window
class Lotto:
    def __init__(self):
        root = Tk()
        root.geometry("325x300")
        root.title("Ithuba National Lottery")

        # date and time
        date = datetime.now()
        date_label = Label(root)
        date_label.grid()
        date_label.config(text="Date" + date.strftime("%d/%m/%y %H:%M"))



        label2 = Label(root, text="Please enter 6 lucky numbers you have chosen")
        label2.grid(columnspan=6)
        # The entries to input 6 lucky numbers
        self.entry2 = Entry(root, textvariable=1, width=2)
        self.entry2.grid(row=2, column=0)

        self.entry3 = Entry(root, textvariable=2, width=2)
        self.entry3.grid(row=2, column=1)

        self.entry4 = Entry(root, textvariable=3, width=2)
        self.entry4.grid(row=2, column=2)

        self.entry5 = Entry(root, textvariable=4, width=2)
        self.entry5.grid(row=2, column=3)

        self.entry6 = Entry(root, textvariable=5, width=2)
        self.entry6.grid(row=2, column=4)

        self.entry7 = Entry(root, textvariable=6, width=2)
        self.entry7.grid(row=2, column=5)

        button8 = Button(root, text="Check lotto numbers", bg="lime green", command=self.won)
        button8.grid(columnspan=6)

        self.text1 = Text(root, width=20, height=2)
        self.text1.grid(row=5, columnspan=6)

        btn1 = Button(root, text="Check Winning Numbers:", bg="lime green", command=self.win)
        btn1.grid(row=6, columnspan=6)

        self.text2 = Text(root, width=20, height=2)
        self.text2.grid(row=7, columnspan=6)

        check_button = Button(root, text="check", bg="red", command=self.check)
        check_button.grid(row=12, column=3)

        self.label_check = Label(root)
        self.label_check.grid()

        self.numbers = []

        root.mainloop()

    # function for button
    def won(self):
        num1 = int(self.entry2.get())
        num2 = int(self.entry3.get())
        num3 = int(self.entry4.get())
        num4 = int(self.entry5.get())
        num5 = int(self.entry6.get())
        num6 = int(self.entry7.get())

        self.userNumbers = [num1, num2, num3, num4, num5, num6]
        userNumbers = self.userNumbers
        userNumbers = sorted(userNumbers)
        # print(userNumbers)

        for a in userNumbers:
            self.text1.insert(END, a)

        return userNumbers

    def win(self):
        lottery = list(range(1, 49))

        numbers = self.numbers

        for i in range(6):
            shuffle(lottery)
            x = lottery.pop()
            numbers.append(x)

            numbers.sort()

            self.text2.delete(1.0, END)
            self.text2.insert(1.0, numbers)
        return numbers

    # function to compare userNumbers and numbers
    def check(self):
        # result = [y for y in self.userNumbers if y in self.numbers]
        counter = 0
        for i in self.userNumbers:
            if i in self.numbers:
                counter += 1
        print(counter)
        # this will display how much money you won
        if int(counter) == 6:
            messagebox.showinfo('result', 'Congratulation you won R10 000 000000')
        if int(counter) == 5:
            messagebox.showinfo('Result', 'You won R8,584.00')
        if int(counter) == 4:
            messagebox.showinfo('result', 'You won R2,384.00')
        if int(counter) == 3:
            messagebox.showinfo('Result', 'You won R100.50')
        if int(counter) == 2:
            messagebox.showinfo('Result', 'You won R20.00')
        if int(counter) == 1:
            messagebox.showinfo('Result', 'R0 - Better luck next time')
        if int(counter) == 0:
            messagebox.showinfo('Result', 'R0 - Better luck next time')+




        # results = open("Lott2.txt", "w+")

        # results.write(str(result))


name = Label(window, text="Please enter your name", bg="lime green")
name.pack()

name_entry = Entry(window)
name_entry.pack()

surname = Label(window, text="Please enter your surname", bg="lime green")
surname.pack()

surname_name = Entry(window)
surname_name.pack()
label1 = Label(window, text="Please enter your age", bg="lime green")

label1.pack()

entry1 = Entry(window)
entry1.pack()

button1 = Button(window, text="PLAY", bg="light blue", command=verify)
button1.pack()

window.mainloop()
