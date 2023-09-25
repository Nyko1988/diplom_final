# def parallel_sent(content:dict):
#     with open('parallel_sent.txt','wt', encoding='utf8') as fOut:
#         fOut.write(source_sentences, target_sentences)
#
#
#     print(content)
#     pass
import re

def read_pages_content_in_parallel(parallel_sent: dict, source_pdf_document, target_pdf_document):
    source_sent = []
    target_sent = []
    for item in parallel_sent:
        start_page_of_source_sent = int(parallel_sent[item]['start_page'])
        final_page_of_source_sent = int(parallel_sent[item]['final page'])
        start_page_of_target_sent = int(parallel_sent[item]['corresponding sentence']['start_page'])
        final_page_of_target_sent = int(parallel_sent[item]['corresponding sentence']['final page'])
        for page in range(start_page_of_source_sent, final_page_of_source_sent):
            content_source = source_pdf_document[page]
            example_content_source = content_source.get_text()
            example_content_source = example_content_source.replace('\n', ' ')
            # Split the text using regular expressions to find spaces followed by one or more digits
            result_source = re.split(r'(\d+)\s+', example_content_source)

            # Remove empty strings from the result
            result_source = [item.strip() for item in result_source if item.strip()]

    print(result_source)
    print('Кількість речень: {}'.format(len(result_source )))
    return result_source
