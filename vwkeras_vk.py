# coding: utf-8
import gensim
import re
import word2veckeras
from gensim.models.word2vec import Word2Vec

sentences =  open(r'vktexts.txt', 'r', encoding='utf-8').read()
sentences = [re.sub("[\W_]+", "", sent) for sent in sentences]
sentences = [sent.split() for sent in sentences]

#model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4, iter =10)
model = Word2VecKeras(sentences , window=5, min_count=5,iter=100)
model.save('model_w2v_vk')
model.wv.save_word2vec_format('model_vk.wv', fvocab='vocab_wv', binary=False)