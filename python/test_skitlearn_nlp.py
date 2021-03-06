# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:24:03 2015

@author: Taikor
"""
categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
    
          
from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset='train',
categories=categories, shuffle=True, random_state=42)


from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_counts.shape


from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape


tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

docs_new = ['take a pill, in god', 'i got a headache']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))
