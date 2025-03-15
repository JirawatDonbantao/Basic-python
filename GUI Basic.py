import tkinter as tk

def set_massage():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('JustPythin')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window, text='wat')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window,text='Okay',command=set_massage)
ok_button.pack()

window.mainloop()