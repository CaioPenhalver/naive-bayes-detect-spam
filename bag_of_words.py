documents = ['Hello, how are you!', 'Win money, win from.', 'Call me now.', 'Hello, Call hello you tomorrow?']

#Convert string to lower case
lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
print(lower_case_documents)

#Remove all punctuation
sans_punctuation_documents = []
import string
for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(string.maketrans('',''), string.punctuation))
print(sans_punctuation_documents)

#Tokenize the strings splitting up a sentence into individual words using a delimiter
preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))
print preprocessed_documents

#Counting the ocurrence of each word in each document
frequency_list = []
import pprint
from collections import Counter
for i in preprocessed_documents:
    frequency_counts = Counter(i)
    frequency_list.append(frequency_counts)
pprint.pprint(frequency_list)
