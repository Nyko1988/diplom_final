from sentence_transformers import SentenceTransformer, util

# Download the vanilla LaBSE model
model = SentenceTransformer('LaBSE')

# Example text in language A and language B
text_in_language_A = "I go home"
text_in_language_B = "я йду додому"

# Encode the text in language A and language B
embeddings_A = model.encode(text_in_language_A, convert_to_tensor=True)
embeddings_B = model.encode(text_in_language_B, convert_to_tensor=True)

# Calculate cosine similarity between the embeddings
similarity_score = util.pytorch_cos_sim(embeddings_A, embeddings_B)

print(f"Similarity Score: {similarity_score}")
