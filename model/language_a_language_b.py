from sentence_transformers import SentenceTransformer, util
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Download the vanilla LaBSE model
model = SentenceTransformer('LaBSE')  # LaBSE
# sbert.net
print(model)
sentences = ["Заряджання акумулятора",
             "Перед першим використанням акумулятора, а також, якщо він не використовувався протягом тривалого часу, потрібно зарядити його.",
             "Дротове заряджання",
             "Підключіть кабель USB до блока живлення USB, а потім вставте кабель у багатофункціональне гніздо пристрою для заряджання акумулятора.",
             "Після повного зарядження від’єднайте зарядний пристрій від мобільного пристрою.",
             "Бездротове заряджання",
             "Пристрій оснащено вбудованою спіраллю для бездротового заряджання. ",
             "Можна заряджати акумулятор за допомогою безпроводового зарядного пристрою (продається окремо).",
             "Перед заряджанням акумулятора складіть пристрій. ",
             "Фактичний час зарядки передбачає, що пристрій не використовується, і може відрізнятися залежно від умов зарядки. ",
             "Якщо (Бездротова передача живлення) на панелі швидкого доступу немає, торкніться і перетягніть кнопку, щоб додати її."]
embeddings = model.encode(sentences)

# Example text in language A and language B
#text_in_language_A = "Charging the battery"
text_in_language_B = "If you cannot find (Wireless power sharing) on the quick panel, tap and drag the button over to add it."

# Encode the text in language A and language B
#embeddings_A = model.encode(text_in_language_A, convert_to_tensor=True)
#embeddings_B = model.encode(text_in_language_B, convert_to_tensor=True)

# Calculate cosine similarity between the embeddings
#similarity_score = util.pytorch_cos_sim(embeddings_A, embeddings_B)


for text_in_language_A in sentences:
    embeddings_A = model.encode(text_in_language_A, convert_to_tensor=True)
    embeddings_B = model.encode(text_in_language_B, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(embeddings_A, embeddings_B)
    print(f"Similarity Score: {similarity_score}", '\t', text_in_language_A)

