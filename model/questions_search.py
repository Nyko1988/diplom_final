from transformers import DPRContextEncoderTokenizer, DPRContextEncoder, \
    DPRQuestionEncoderTokenizer, DPRQuestionEncoder
import torch
from sentence_transformers.util import cos_sim

ctx_model = DPRContextEncoder.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')
ctx_tokenizer = DPRContextEncoderTokenizer.from_pretrained('facebook/dpr-ctx_encoder-single-nq-base')

question_model = DPRQuestionEncoder.from_pretrained('facebook/dpr-question_encoder-single-nq-base')
question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained('facebook/dpr-question_encoder-single-nq-base')

questions = ["What is the capital city of australia?",
             "What is the best selling sci-fi book?"]

contexts = ["the best-selling sci-fi book is dune",
            "Google is a popular search engine",
            "canberra is the capital city of australia"]

xb_tokens = ctx_tokenizer(contexts, max_length=256, padding='max_length', return_tensors='pt')
xb = ctx_model(**xb_tokens)

xq_tokens = question_tokenizer(questions, max_length=256, padding='max_length', return_tensors='pt')
xq = question_model(**xq_tokens)

xq.keys()
x = xq.pooler_output.shape
print(x)

for i, xq_vec in enumerate(xq.pooler_output):
    probs = cos_sim(xq_vec, xb.pooler_output)
    argmax = torch.argmax(probs)
    print(questions[i])
    print(contexts[argmax])
    print('--')