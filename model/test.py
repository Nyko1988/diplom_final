import datasets

all_datasets = datasets.list_datasets()

# Фильтруйте датасеты, которые поддерживают украинский и английский языки
ukrainian_datasets = []
english_datasets = []
dataset_name = 'ted_talks_iwslt'

dataset = datasets.load_dataset(dataset_name, 'eu_ca_2014', split='train')

languages = dataset[0]['translations']['language']

if 'uk' in languages:
    ukrainian_datasets.append(dataset_name)
if 'en' in languages:
    english_datasets.append(dataset_name)
