import fitz
import re
import sys, pathlib, fitz

# pdf = fitz.open('D:/University/Flex/SM-F721B_UM_CIS_TT_Ukr_Rev.2.0_230210.pdf')
# document_page_numbers = pdf.page_count  # кількість сторінок
# start_page_of_content = 1
# final_page_of_content = 4
# dict_of_pages = {}
# def dict_of_content(start_page_of_content, final_page_of_content):
#     result_dict = {}
#     for page_old in range(start_page_of_content, final_page_of_content):
#         content = pdf[page_old]
#         example_content = content.get_text()
#         example_content = example_content.replace('\n', ' ')
#         # Split the text using regular expressions to find spaces followed by one or more digits
#         result = re.split(r'(\d+)\s+', example_content)
#
#         # Remove empty strings from the result
#         result = [item.strip() for item in result if item.strip()]
#
#         # Create a dictionary from the result
#         prev_was_number = False
#         for i in range(len(result) - 1):
#             if not prev_was_number:
#                 if result[i].isdigit() and result[i + 1].isdigit() is not True:
#                     result_dict[result[i]] = result[i + 1]
#                     prev_was_number = True
#             else:
#                 prev_was_number = False
#         return result_dict
#
#     # Print the dictionary
# print(dict_of_content(start_page_of_content, final_page_of_content))
#
# pdf.close()


def test():
    fname = sys.argv[0]  # get document filename
    with fitz.open('D:/University/Flex/SM-F721B_UM_CIS_TT_Ukr_Rev.2.0_230210.pdf') as doc:  # open document
        text = chr(12).join([page.get_text() for page in doc])
        print(text)
    # write as a binary file to support non-ASCII characters
    x = pathlib.Path(fname + ".txt").write_bytes(text.encode())
    print(x)

test = test()