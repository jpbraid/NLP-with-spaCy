import pandas as pd
from spacy.lang.en import English

nlp = English()
doc = nlp("Hello world!")

for token in doc:
    print(token.text)
token = doc[1]
print(token.text)

f = open('data/yelp/v6/yelp_academic_dataset_review.json')
js = []

for i in range(10000):
    js.append(json.loads(f.readline()))
    
f.close()
review_df = pd.DataFrame(js)
bow_converter = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')

