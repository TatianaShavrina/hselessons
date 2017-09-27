import re
import pandas as pd
import gensim as gs
from pymystem3 import Mystem
from sklearn.feature_extraction.text import *

path1 = r"/home/mi_air/Documents/SAS/Готовое/Задание1/investfunds2500.csv"
investfunds = pd.read_csv(path1, sep="\t")


path2 = r"/home/mi_air/Documents/SAS/Готовое/Задание1/prodengi2500.csv"
prodengi = pd.read_csv(path2, sep="\t")


m = Mystem()
mystopwords = []
stop = open(r"/home/mi_air/stopwords_russian.txt", "r", encoding="utf8")
for line in stop:
    mystopwords.append(line.strip("\n"))
punct = "-—=+&^%$#@!()[]*.<?>,_«»1234567890 "
for i in punct:
    mystopwords.append(i)

global mystopwords
global punct

#лемматизируем корпус
def lemmatize(text):
    return(m.lemmatize(text))

#удалим стоп-слова (после лемматизации, так как иной порядок может повредить лемматизации)
def stopwords(lst):
    stopwords=mystopwords
    try:
        return ([token for token in lst if not token in stopwords])
    except:
        return [""]

nostop1, nostop2 = [],[]
for i in range(2500):   
    nostop1.append(" ".join(stopwords(lemmatize(investfunds.article.iloc[i]))))
    nostop2.append(" ".join(stopwords(lemmatize(prodengi.article.iloc[i]))))
investfunds["lemmas_no_stopwords"] = nostop1
prodengi["lemmas_no_stopwords"] = nostop2

#функция для преобразования данных в объек gensim и фиттинг модели

def topic_modeling(series):
    vectorizer = CountVectorizer(max_features=300000)
    corpus_tfidf_unsuper = vectorizer.fit_transform(series)
    #трансформируем в объект для gensim 
    vocab = vectorizer.get_feature_names()
    id2word_unsuper=dict([(i, s) for i, s in enumerate(vocab)])
    corpus_vect_gensim_unsuper = gs.matutils.Sparse2Corpus(corpus_tfidf_unsuper.T)
    #фиттим модель
    lda = gs.models.LdaModel(corpus_vect_gensim_unsuper, 
                  id2word = id2word_unsuper, 
                  num_topics = 25, 
                  passes=10, random_state=42)
    print("gone 10 passes")
    topwords = lda.print_topics(-1)
    return(topwords) #список кортежей "номер темы + термины"

#тематическое моделирование на investfunds
topwords_investfund = topic_modeling(investfunds["lemmas_no_stopwords"])
table1 = open( r"/home/mi_air/Documents/SAS/Готовое/Задание1/investfunds_topic_table.csv", "w", encoding="utf8")
table1.write("topic number\tterms\n")
for pair in topwords_investfund:
    terms = [re.split('\*"',re.split('" ', item)[0])[1] for item in re.split("\+", pair[1])]
    table1.write(str(pair[0])+"\t"+", ".join(terms)+"\n")
    #print(pair)

#тематическое моделирование на prodengi
topwords_prodengi = topic_modeling(prodengi["lemmas_no_stopwords"])
table2 = open( r"/home/mi_air/Documents/SAS/Готовое/Задание1/prodengi_topic_table.csv", "w", encoding="utf8")
table2.write("topic number\tterms\n")
for pair in topwords_prodengi:
    terms = [re.split('\*"',re.split('" ', item)[0])[1] for item in re.split("\+", pair[1])]
    table2.write(str(pair[0])+"\t"+", ".join(terms)+"\n")
    #print(pair)
