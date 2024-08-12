from tkinter import *
root = Tk()

root.title('My Box GUI')
root.iconbitmap('waffleicon.ico')
root.geometry("750x750")

value = None
button1_clicked = False
fishchance = 0
def testfunc1():
    my_label2 = Label(root, text = fishchance, font=("Arial", 25))
    my_label2.grid(row = 5, column = 3)


my_label = Label(root, text = 'Waffles')

mybutton = Button(root, text = 'Button 1',command = testfunc1, font=("Arial", 15))


my_label.grid(row=0,column=1)

mybutton.grid(row=0,column=3)

root.mainloop()

