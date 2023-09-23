import datasets
from sentence_transformers import InputExample, models, SentenceTransformer, ParallelSentencesDataset
from transformers import XLMRobertaTokenizer, BertTokenizer
from tqdm.auto import tqdm
import gzip
import os
from torch.utils.data import DataLoader
from sentence_transformers.losses import MSELoss

ted = datasets.load_dataset('ted_multi', split='train')
print(ted[0])
idx = ted[0]['translations']['language'].index('en')
print(idx)
source = ted[0]['translations']['translation'][idx]
print(source)
pairs = []
for i, translation in enumerate(ted[0]['translations']['translation']):
    if i != idx:
        pairs.append((source, translation))

print(pairs[1])
#initialize list of languages to keep
lang_list = ['ru', 'es', 'ar', 'fr', 'de']
#create dict to store our pairs
train_samples = {f'en-{lang}': [] for lang in lang_list}

#now build our training samples list
for row in tqdm(ted):
    #get source (English)
    idx = row['translations']['language'].index('en')
    source = row['translations']['translation'][idx].strip()
    #loop through translations
    for i,lang in enumerate(row['translations']['language']):
        #check if the lang is in lang list
        if lang in lang_list:
            translation = row['translations']['translation'][i].strip()
            train_samples[f'en-{lang}'].append(source+'\t'+translation)

#how many pairs for each language?
for lang_pair in train_samples.keys():
    print(f'{lang_pair}: {len(train_samples[lang_pair])}')

print(source+'\t'+translation)

#create dir
if not os.path.exists('./examp'):
    os.mkdir('./examp')

#save to file, sentence transformers reader will expect tsv.gz file
for lang_pair in train_samples.keys():
    with gzip.open(f'./examp/ted-train-{lang_pair}.tsv.gz', 'wt', encoding='utf-8') as f:
        f.write('\n'.join(train_samples[lang_pair]))


xlmr_tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-base')
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentences = ['I will attend the meeting at 11 pm',
             'Я прийду на засідання о 23:00']
for text in sentences:
    print(xlmr_tokenizer.tokenize(text))


xlmr = models.Transformer('xlm-roberta-base')
polling = models.Pooling(xlmr.get_word_embedding_dimension(), pooling_mode_mean_tokens=True)

student = SentenceTransformer(modules=[xlmr, polling])
print(student)


teacher = SentenceTransformer('paraphrase-distilroberta-base-V2')

data = ParallelSentencesDataset(student_model=student, teacher_model=teacher,
                                batch_size=68, use_embedding_cache=True)
train_files = os.listdir('./examp/')
for f in train_files:
    print(f)
    data.load_data('./examp/'+f, max_sentences=500_000, max_sentence_length=256)

loader = DataLoader(data, shuffle=True, batch_size=68)
loss = MSELoss(model=student)

student.fit(train_objectives=[(loader, loss)],
            epochs=1,
            warmup_steps=int(len(loader) * 0.1),
            output_path='./xlmr-ted',
            optimizer_params={'lr': 2e-5, 'eps':1e-6},   #, 'correct_bias':False
            save_best_model=True)

