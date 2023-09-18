import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty')

def del_entry():
    name.delete(0, tk.END)

def submit():
    print(name.get())
    print(name_second.get())


win = tk.Tk()
win.title('Par corpus')
#photo = tk.PhotoImage(file='icon.png')
#win.iconphoto(False, photo)
win.config(bg='white')
win.geometry("700x600+10+10")

# Виджет Entry
tk.Label(win, text='First page').grid(row=0, column=0, sticky='w')
tk.Label(win, text='Second page').grid(row=1, column=0, sticky='w')
name = tk.Entry(win)
name_second = tk.Entry(win)
name.grid(row=0, column=1)
name_second.grid(row=1, column=1)

tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, sticky='we')
tk.Button(win, text='delete', command=del_entry).grid(row=2, column=1, sticky='we')
tk.Button(win, text='Submit', command=submit).grid(row=3, column=0, sticky='we')
tk.Button(win, text='insert', command=lambda : name.insert(0, 'Hello')).grid(row=2, column=2, sticky='we')

win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=100)
win.mainloop()
