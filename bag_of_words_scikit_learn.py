documents = ['Hello, how are you!', 
        'Win money, win from home.', 
        'Call me now.', 
        'Hello, Call hello you tomorrow?']

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

count_vector = CountVectorizer()
count_vector.fit(documents)
doc_array = count_vector.transform(documents).toarray()
frequency_matrix = pd.DataFrame(doc_array, columns = count_vector.get_feature_names())
print frequency_matrix


