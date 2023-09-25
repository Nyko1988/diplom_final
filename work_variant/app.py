import re
import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF library
from PIL import Image
from PIL import ImageTk
from compare_sent import create_paralel_sent
from parallel_sent import read_pages_content_in_parallel


class PDFViewerApp:
    def __init__(self, root):
        self.pdf_document = None
        self.source_pdf_document = None
        self.target_pdf_document = None
        self.content_ukr_file = {}
        self.content_eng_file = {}
        self.content_common_file = {}
        self.root = root
        self.root.title("Parallel corpus helper")
        self.root.geometry("1500x700")
        tk.PhotoImage(file='icon.png')

        self.my_menu = tk.Menu(root)
        self.root.config(menu=self.my_menu)

        self.file_menu = tk.Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open PDF file", command=self.open_pdf)
        self.file_menu.add_command(label="Clear", command=self.clear_canvas)
        self.file_menu.add_command(label="Quit", command=self.quit_app)

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.pdf_images = []  # To hold PhotoImage objects

        frame2 = tk.LabelFrame(text='Pages of content', width=300, height=100)
        frame2.pack(padx=30, pady=10)
        # create first label
        label_entry_first_row_of_content = tk.Label(frame2, text='First Page', font=('Arial', 7, 'bold'), width=10,
                                                    height=3)
        label_entry_first_row_of_content.grid(row=0, column=0, sticky='n', padx=1, pady=1)

        # create second label
        label_entry_second_row_of_content = tk.Label(frame2, text='Last Page', font=('Arial', 7, 'bold'), width=10,
                                                     height=3)
        label_entry_second_row_of_content.grid(row=1, column=0, sticky='n', padx=1, pady=1)

        # create button read ukr file
        button_read_ukr_file = tk.Button(frame2, text='Read content ukr file', width=20,
                                         command=lambda: self.read_pages_content(self.content_ukr_file,
                                                                                 True))
        button_read_ukr_file.grid(row=2, column=0, columnspan=2, padx=1, pady=1)

        # create button read eng file
        button_read_eng_file = tk.Button(frame2, text='Read content eng file', width=20,
                                         command=lambda: self.read_pages_content(self.content_eng_file,
                                                                                 False))
        button_read_eng_file.grid(row=3, column=0, columnspan=2, padx=1, pady=1)

        # create button compare content
        button_compare_content = tk.Button(frame2, text='Compare content', width=20,
                                           command=lambda: create_paralel_sent(self.content_ukr_file,
                                                                               self.content_eng_file,
                                                                               self.content_common_file))
        button_compare_content.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        # create button compare sentences
        button_compare_sent = tk.Button(frame2, text='Compare sentences', width=20,
                                        command=lambda: read_pages_content_in_parallel(self.content_common_file,
                                                                                       self.source_pdf_document,
                                                                                       self.target_pdf_document))
        button_compare_sent.grid(row=5, column=0, columnspan=2, padx=1, pady=1)

        # create first widget entry
        self.entry_first_row_of_content = tk.Entry(frame2, justify=tk.RIGHT, font=('Arial', 15), width=10)
        self.entry_first_row_of_content.insert(0, '')
        self.entry_first_row_of_content.grid(row=0, column=1, sticky='n', padx=10, pady=10)

        # create second widget entry
        self.entry_second_row_of_content = tk.Entry(frame2, justify=tk.RIGHT, font=('Arial', 15), width=10)
        self.entry_second_row_of_content.insert(0, '')
        self.entry_second_row_of_content.grid(row=1, column=1, sticky='n', padx=10, pady=10)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(title="Select a PDF",
                                               filetype=(("PDF Files", "*.pdf"), ("All Files", "*.*")))

        if file_path:
            self.pdf_document = fitz.open(file_path)
            self.display_pdf(self.pdf_document)

    def display_pdf(self, pdf_document):
        self.clear_canvas()
        self.pdf_images = []  # Clear previous images

        total_height = 0
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            img = self.get_page_image(page)
            img_height = img.height()

            self.canvas.create_image(0, total_height, anchor=tk.NW, image=img)
            total_height += img_height

            self.pdf_images.append(img)  # Store the image to prevent it from being garbage collected

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def get_page_image(self, page):
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img = self.pixmap_to_photo(pix)
        return img

    def pixmap_to_photo(self, pixmap):
        img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        photo = ImageTk.PhotoImage(image=img)

        return photo

    def read_pages_content(self, result_dict, pdf_document_set):
        """читаємо зміст і наповнюємо словник де ключ є сторінка а значення - назва розділу"""
        start_page_of_content = int(self.entry_first_row_of_content.get()) - 1
        final_page_of_content = int(self.entry_second_row_of_content.get())
        doc = self.pdf_document

        for page in range(start_page_of_content, final_page_of_content):
            content = doc[page]
            example_content = content.get_text()
            example_content = example_content.replace('\n', ' ')
            # Split the text using regular expressions to find spaces followed by one or more digits
            result = re.split(r'(\d+)\s+', example_content)

            # Remove empty strings from the result
            result = [item.strip() for item in result if item.strip()]

            # Create a dictionary from the result
            prev_was_number = False
            for i in range(len(result) - 1):
                if not prev_was_number:
                    if result[i].isdigit() and result[i + 1].isdigit() is not True:
                        temp_dict = {'start_page': result[i],
                                     'final page': result[i + 2] if i + 2 < len(result) else len(doc),
                                     'next section': result[i + 3] if i + 3 < len(result) else '-'}
                        result_dict[(result[i + 1])] = temp_dict
                        prev_was_number = True
                else:
                    prev_was_number = False

        if pdf_document_set:
            self.source_pdf_document = self.pdf_document
        else:
            self.target_pdf_document = self.pdf_document
        print(result_dict)
        print('Кількість пунктів меню: {}'.format(len(result_dict)))
        return result_dict, pdf_document_set

    # compare_comtent = create_paralel_sent()

    def clear_canvas(self):
        self.canvas.delete("all")
        # for img in self.pdf_images:
        #     img.blank()  # Clear the PhotoImage objects

        self.pdf_images = []  # Clear the list

    def quit_app(self):
        self.root.destroy()


def main():
    root = tk.Tk()
    app = PDFViewerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
