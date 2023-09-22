from sentence_transformers import SentenceTransformer, util
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Download the vanilla LaBSE model
model = SentenceTransformer('all-mpnet-base-V2') #LaBSE
#sbert.net
print(model)
sentences = ["After fully charging, disconnect the charger from the device.",
    "Wireless charging",
    "The device has a built-in wireless charging coil.",
    "You can charge the battery using a wireless charger (sold separately).",
    "Fold the device before charging the battery."]
embeddings = model.encode(sentences)
print(embeddings[0])
print(embeddings.shape) #(5, 768) 5->embeddings(sentences), кожне 768 dimensions

sim = np.zeros((len(sentences), len(sentences)))
for i in range(len(sentences)):
    sim[i:, i] = util.cos_sim(embeddings[i], embeddings[i:])
print(sim)


sns.heatmap(sim, annot=True)