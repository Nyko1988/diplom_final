from fitz import *

with fitz.open('D:/Useful Manuals/University/Flex/SM-F721B_UM_EU_TT_Eng_Rev.2.0_230126.pdf') as file:
    page = file.load_page(10)
    content = page.get_text()
    print(content.split('\n'))
from sentence_transformers import SentenceTransformer, util
ukr = """Початок роботи
Заряджання акумулятора
Перед першим використанням акумулятора, а також, якщо він не використовувався протягом тривалого часу, потрібно зарядити його.
Дротове заряджання
Підключіть кабель USB до блока живлення USB, а потім вставте кабель у багатофункціональне гніздо пристрою для заряджання акумулятора. Після повного зарядження від’єднайте зарядний пристрій від мобільного пристрою.
Бездротове заряджання
Пристрій оснащено вбудованою спіраллю для бездротового заряджання. Можна заряджати акумулятор за допомогою безпроводового зарядного пристрою (продається окремо).
Перед заряджанням акумулятора складіть пристрій. Сумістіть центр задньої панелі пристрою із центром бездротового зарядного пристрою для заряджання акумулятора. Після повного зарядження акумулятора від’єднайте зарядний пристрій від бездротового зарядного пристрою.
Розрахований час зарядки буде відображено на панелі сповіщень. Фактичний час зарядки передбачає, що пристрій не використовується, і може відрізнятися залежно від умов зарядки. 
Бездротове заряджання може не працювати належним чином через певний аксесуар або кришку. 
Для надійного бездротового заряджання рекомендується зняти таку кришку або аксесуар з пристрою.
Щоб забезпечити належне з’єднання, відкоригуйте положення пристроїв для розташування їх належним чином, як показано на зображенні нижче. 
Інакше пристрій може не заряджатися належним чином або може перегріватися.
Getting started
Charging the battery
Charge the battery before using it for the first time or when it has been unused for extended 
periods.
Wired charging
Connect the USB cable to the USB power adaptor and plug the cable into the device’s 
multipurpose jack to charge the battery. 
After fully charging, disconnect the charger from the 
device.
Wireless charging
The device has a built-in wireless charging coil. You can charge the battery using a wireless 
charger (sold separately).
Fold the device before charging the battery. Place the centre of the device’s back on the 
centre of the wireless charger to charge the battery. After fully charging, disconnect the 
device from the wireless charger.
The estimated charging time will appear on the notification panel. The actual charging time 
assumes that the device is not in use, and it may vary depending on the charging conditions. 
Wireless charging may not work smoothly depending on the type of accessory or cover. 
For stable wireless charging, it is recommended to separate the cover or accessory from the 
device.
Adjust the devices into the correct position as shown in the image below to ensure 
that their connection is good. Otherwise, the device may not charge properly or may 
overheat."""
sent1 = ukr.split('.')
model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = sent1
#Encode all sentences
embeddings = model.encode(sentences)

#Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings, embeddings)

#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append([cos_sim[i][j], i, j])

#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

print("Top-5 most similar pairs:")
for score, i, j in all_sentence_combinations[0:5]:
    print("{} \t {} \t {:.4f}".format(sentences[i], sentences[j], cos_sim[i][j]))