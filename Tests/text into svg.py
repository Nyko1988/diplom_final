import fitz  # Импорт библиотеки PyMuPDF (Fitz)

def get_pdf_page_size(pdf_path):
    pdf_document = fitz.open(pdf_path)  # Открытие PDF-файла
    first_page = pdf_document[0]  # Получение первой страницы
    page_size = first_page. # Получение размера страницы
    pdf_document.close()  # Закрытие PDF-файла
    return page_size

# Укажите путь к вашему PDF-файлу
pdf_path = 'D:/Useful Manuals/University/SM-F721B_UM_CIS_TT_Ukr_Rev.2.0_230210.pdf'
page_size = get_pdf_page_size(pdf_path)

# Размер страницы задается в точках (1 дюйм = 72 точки)
width_in_points = page_size[2] - page_size[0]
height_in_points = page_size[3] - page_size[1]

# Печать размера страницы
print(f"Ширина страницы: {width_in_points} точек")
print(f"Высота страницы: {height_in_points} точек")
