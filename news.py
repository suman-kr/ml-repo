from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np

print fetch_20newsgroups
categories = ['alt.atheism','soc.religion.christian','comp.graphics','sci.med']
x_train = fetch_20newsgroups(subset='train',categories=categories,shuffle=True,random_state=42)
text_clf = Pipeline([('a',CountVectorizer()),('b',TfidfTransformer()),('c',MultinomialNB())])
text_clf.fit(x_train.data,x_train.target)
x_test = fetch_20newsgroups(subset='test',categories=categories,shuffle=True,random_state=42)
predict = text_clf.predict(x_test.data)
print np.mean(predict == x_test.target)
print metrics.classification_report(x_test.target,predict,target_names=x_test.target_names)
print metrics.confusion_matrix(x_test.target,predict)