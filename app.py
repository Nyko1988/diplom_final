import tkinter as tk


def say_hello():
    print('Hello')


def add_label():
    label = tk.Label(win, text='test')
    label.pack()

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty')

win = tk.Tk()
win.title('Par corpus')
photo = tk.PhotoImage(file='Tests/icon.png')
win.iconphoto(False, photo)
win.config(bg='white')
win.geometry("700x600+10+10")

# # Виджет Label
# label_1 = tk.Label(win, text="Label",
#                    bg='white',
#                    fg='black',
#                    font=('Arial', 20, 'bold'),
#                    # padx=10,
#                    # pady=10
#                    width=10,
#                    height=1,
#                    relief=tk.RAISED)
# label_1.pack()
#
# btn1 = tk.Button(win, text='say hello',
#                  command=say_hello)
#
# btn2 = tk.Button(win, text='add label',
#                  command=add_label)
# btn3 = tk.Button(win, text='Add new label lambda',
#                  command=lambda: tk.Label(win, text='new lambda').pack())
#

# btn1.pack()
# btn2.pack()
# btn3.pack()

# # #как размещать виджеты при помощи метода grid()
# btn1 = tk.Button(win, text='Hello 1')
# btn2 = tk.Button(win, text='Hello 2')
# btn3 = tk.Button(win, text='Hello 3')
# btn4 = tk.Button(win, text='Hello 4')
# btn5 = tk.Button(win, text='Hello 5')
#
# btn1.grid(column=0, row=0)
# btn2.grid(column=0, row=1, sticky='w')
# btn3.grid(column=1, row=0)
# btn4.grid(column=1, row=1, sticky='w')
# btn5.grid(column=2, row=0, rowspan=2, sticky='s')

#Виджет Entry
tk.Label(win, text='Name').grid(row=0, column=0, sticky='w')
name = tk.Entry(win)
name.grid(row=0, column=5)

tk.Button(win, text='get', command=get_entry).grid(row=1, column=0)

win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=100)
win.mainloop()
