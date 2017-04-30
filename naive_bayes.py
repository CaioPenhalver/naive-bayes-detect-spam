import pandas as pd
df = pd.read_table('SMSSpamCollection',
                    sep='\t',
                    header=None,
                    names=['label', 'sms_message'])
df['label'] = df.label.map({'ham':0, 'spam':1})
print df.shape
print df.head()

from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(df['sms_message'], df['label'], random_state=1)

print('number of rows in the total set: {}'.format(df.shape[0]))
print('number of rows in the traning set: {}'.format(x_train.shape[0]))
print('number of rows in the test set: {}'.format(x_test.shape[0]))

from sklearn.feature_extraction.text import CountVectorizer

# Instantiate the CountVectorizer method
count_vector = CountVectorizer()

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(x_train)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data = count_vector.transform(x_test)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)
predictions = naive_bayes.predict(testing_data)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
print('Precision score: ', format(precision_score(y_test, predictions)))
print('Recall score: ', format(recall_score(y_test, predictions)))
print('F1 score: ', format(f1_score(y_test, predictions)))
