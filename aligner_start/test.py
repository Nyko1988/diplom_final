from lingtrain_aligner import splitter, aligner, resolver, metrics
lang_from = "en"
lang_to = "ua"
db_path = "alignment.db"

text1=""""""
text2=""""""
splitted_from = splitter.split_by_sentences(text1.split('\n'), lang_from)
splitted_to = splitter.split_by_sentences(text2.split('\n'), lang_to)

aligner.fill_db(db_path, lang_from, lang_to, splitted_from, splitted_to)