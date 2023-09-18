import tkinter as tk
from tkinter import filedialog, scrolledtext, END, WORD, LEFT, RIGHT, TOP, NW
import pdfplumber

# Create an instance of tkinter frame
win = tk.Tk()
# Set the Geometry
win.geometry("1500x700")
# Create a Text Box
text = scrolledtext.ScrolledText(win, wrap=WORD, width=150, height=50)
text.pack(padx=10, pady=10, side=RIGHT)

frame2 = tk.LabelFrame(text='Some operations', width=300, height=100)
frame2.pack(padx=30, pady=10)
#create first label
label_entry_first_row_of_content = tk.Label(frame2, text='First row', font=('Arial', 7, 'bold'), width=10, height=3)
label_entry_first_row_of_content.grid(row=0, column=0, sticky='n', padx=1, pady=1)

#create second label
label_entry_second_row_of_content = tk.Label(frame2, text='Last row', font=('Arial', 7, 'bold'), width=10, height=3)
label_entry_second_row_of_content.grid(row=1, column=0, sticky='n', padx=1, pady=1)

#create button start
button_start = tk.Button(frame2, text='START', width=10)
button_start.grid(row=2, column=0, columnspan=2, padx=1, pady=1)

#create first widget entry
entry_first_row_of_content = tk.Entry(frame2, justify=tk.RIGHT, font=('Arial', 15), width=10)
entry_first_row_of_content.insert(0, '')
entry_first_row_of_content.grid(row=0, column=1, sticky='n', padx=10, pady=10)

#create second widget entry
entry_second_row_of_content = tk.Entry(frame2, justify=tk.RIGHT, font=('Arial', 15), width=10)
entry_second_row_of_content.insert(0, '')
entry_second_row_of_content.grid(row=1, column=1, sticky='n', padx=10, pady=10)


# Define a function to clear the text
def clear_text():
    text.delete(1.0, END)


# Define a function to open the pdf file
def open_pdf():
    file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
    lines = []
    final_content = ''
    if file:
        with pdfplumber.open(file) as pdf:
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                content = page.extract_text(x_tolerance=1, x_density=4, y_density=12, layout=True, )
                lines.extend(content.split('\n'))
                final_content += content
        text.insert(1.0, final_content)
    return lines



# Define function to Quit the window
def quit_app():
    win.destroy()


# Create a Menu
my_menu = tk.Menu(win)
win.config(menu=my_menu)

# Add dropdown to the Menus
file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open file in ukr", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_command(label="Quit", command=quit_app)
win.mainloop()
