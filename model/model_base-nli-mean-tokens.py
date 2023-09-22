from sentence_transformers import SentenceTransformer, util
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Download the vanilla LaBSE model
model = SentenceTransformer('bert-base-nli-mean-tokens') #LaBSE
#sbert.net
print(model)
sentences = ["After fully charging, disconnect the charger from the device.",
    "Wireless charging",
    "The device has a built-in wireless charging coil.",
    "You can charge the battery using a wireless charger (sold separately).",
    "Fold the device before charging the battery."]
embeddings = model.encode(sentences)
print(embeddings)
print(embeddings.shape) #(5, 768) 5->embeddings(sentences), кожне 768 dimensions

sim = np.zeros((len(sentences), len(sentences)))
for i in range(len(sentences)):
    sim[i:, i] = util.cos_sim(embeddings[i], embeddings[i:])
print(sim)


sns.heatmap(sim, annot=True)

# # Example text in language A and language B
# text_in_language_A = "I go home"
# text_in_language_B = "я йду додому"
#
# # Encode the text in language A and language B
# embeddings_A = model.encode(text_in_language_A, convert_to_tensor=True)
# embeddings_B = model.encode(text_in_language_B, convert_to_tensor=True)
#
# # Calculate cosine similarity between the embeddings
# similarity_score = util.pytorch_cos_sim(embeddings_A, embeddings_B)
#
# print(f"Similarity Score: {similarity_score}")
