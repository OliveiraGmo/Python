from tkinter import Tk ,Label,PhotoImage
root = Tk()
photo=PhotoImage(file='adventure-time-jake.gif').subsample(5)
hello = Label(master=root,text='Aprendendo GUIs')
hello.pack()
root.mainloop()
#incrementando

