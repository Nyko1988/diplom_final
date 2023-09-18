import os
import pickle

from functorch._src.aot_autograd import model_name
from sentence_transformers import SentenceTransformer

model = pickle.load(open(
    'C:/Users\MMykytiuk/.cache/torch/sentence_transformers/sentence-transformers_all-MiniLM-L6-v2/pytorch_model.bin',
    'rb'))
# @param ["LaBSE (Ukrainian-English fine-tuned)", "LaBSE", "Sentence Transformers DistilUSE multilingual v2"]

model_names = {
    "LaBSE (Ukrainian-English fine-tuned)": 'labse_uk_en',
    "LaBSE": 'labse',
    "Sentence Transformers DistilUSE multilingual v2": 'st2'
}

if model_names[model_name] == 'labse_uk_en':
    if not os.path.isfile('/content/best_model_uk_en.bin'):
        # Download or specify the path to your Ukrainian-English fine-tuned model.
        # You may need to provide a download link or specify a local file path.
        pass
    model = pickle.load(open('/content/best_model_uk_en.bin', 'rb'))
elif model_names[model_name] == 'st2':
    model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
else:
    model = SentenceTransformer('LaBSE')
