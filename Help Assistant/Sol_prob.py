#importing libraries
import nltk
import numpy as np

#Downloading packages

# downloading model to tokenize message
nltk.download('punkt')
# downloading stopwords
nltk.download('stopwords')
# downloading wordnet, which contains all lemmas of english language,that is the root form of words
nltk.download('wordnet')

#importing tokenizer stopwords and lemmatizer from nltk
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
#print(stop_words)

from nltk.stem import WordNetLemmatizer

#Function to clean the text
def clean_corpus(corpus):
  # lowering every word in text
  corpus = [ doc.lower() for doc in corpus]
  cleaned_corpus = []
  
  stop_words = stopwords.words('english')
  wordnet_lemmatizer = WordNetLemmatizer()

  # iterating over every text[a,b,c]='a b c'
  for doc in corpus:
    # tokenizing text
    tokens = word_tokenize(doc)
    cleaned_sentence = [] 
    for token in tokens: 
      # removing stopwords, and punctuation
      if token not in stop_words and token.isalpha(): 
        # applying lemmatization
        cleaned_sentence.append(wordnet_lemmatizer.lemmatize(token)) 
    cleaned_corpus.append(' '.join(cleaned_sentence))
  return cleaned_corpus
  
  #Loading our intents
  import json
with open('intents.json', 'r') as file:
  intents = json.load(file)

  #Cleaning our Intents
  corpus = []
tags = []

for intent in intents['intents']:
    # taking all patterns in intents to train a neural network
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])
cleaned_corpus = clean_corpus(corpus)
#cleaned_corpus

#Intents Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
vz= TfidfVectorizer()
X = vz.fit_transform(cleaned_corpus)
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
y = enc.fit_transform(np.array(tags).reshape(-1,1))

#Traning neural network
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential([
                    Dense(128, input_shape=(X.shape[1],), activation='relu'),
                    Dropout(0.2),
                    Dense(64, activation='relu'),
                    Dropout(0.2),
                    Dense(y.shape[1], activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

history = model.fit(X.toarray(), y.toarray(), epochs=20, batch_size=1)

# if prediction for every tag is low, then we want to classify that message as noanswer

INTENT_NOT_FOUND_THRESHOLD = 0.40

def predict_intent_tag(message):
  message = clean_corpus([message])
  X_test = vectorizer.transform(message)
  #print(message)
  #print(X_test.toarray())
  y = model.predict(X_test.toarray())
  #print (y)
  # if probability of all intent is low, classify it as noanswer
  if y.max() < INTENT_NOT_FOUND_THRESHOLD:
    return 'noanswer'
  
  prediction = np.zeros_like(y[0])
  prediction[y.argmax()] = 1
  tag = encoder.inverse_transform([prediction])[0][0]
  return tag
  
 