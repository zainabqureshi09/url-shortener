import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="blue")


# button function

def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END, s)


Label(win, text="Enter your URL link", font="impact 17 bold", bg="black", fg="white").pack(fill="x")

entry1 = Entry(win, font="10", bd=3, width=40)
entry1.pack(pady=30)

Button(win, text="Click Me", font="impact 12 bold", bg="blue", fg="white", width="14", command=short).pack()

entry2 = Entry(win, font="impact 16 bold", bg="pink", width=24, bd=0)
entry2.pack(pady=30)
mainloop()
