#!/usr/bun/env python


##### Look inro TFIDF to remove very common words ####

# import modules
import csv
from langdetect import detect
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

tokenizer = RegexpTokenizer(r'\w+')

# get the english stop words list
enStop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# create list and dictionaries for processesing the documents
docSet = []
docDic = {}
langList = []
langDic = {}
esSet = []

# load the csv with the documents (1 per row)
with open('./dprkSlogans.csv', 'r') as docs:
    reader = csv.reader(docs)
    for row in reader:
        docSet.append(unicode(''.join(row), 'utf-8'));

# record how many documents are in the analsysis
docLen = len(docSet)

# create a dictionary of the documents: index:documenet text
for i in range(0, docLen):
    docDic[i] = docSet[i];

# create a dictionary of the documents and the detected language
for i in docDic:
    langDic[i] = detect(docDic[i])

uniqueLang = set (langDic.values())

# create list of non-english documents
for doc, lang in langDic.items():
    if lang != 'en':
        esSet.append(doc);

# remove the non-english documents from the analsysis

ldaSet = []
for k, v in docDic.iteritems():
    if k not in esSet:
        ldaSet.append(v)

texts = []

# loop through the list of documents in ldsSet and clean up the text
for i in ldaSet:
    #detect language
    detect(i)
    #lowercase all text and tokenize it
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from the tokens
    stoppedTokens = [i for i in tokens if not i in enStop]
    # stem tokens
    stemmedTokens = [p_stemmer.stem(i) for i in stoppedTokens]

    texts.append(stemmedTokens)

# print texts

# turn tokenized docs into an id term dictionary
dictionary = corpora.Dictionary(texts)

# print dictionary

#convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# print corpus

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=150)

print(ldamodel.print_topics(num_topics=8, num_words=8))

print ('### REPORT ###')
print('There are: %d documents in this analysis' % len(docSet))
print('There are: %d language(s) in this analysis' % len(uniqueLang))


# create English stop words list
stopWords = get_stop_words('en')
