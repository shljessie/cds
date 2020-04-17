import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import nltk
import re
import pandas as pd
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from itertools import islice

df = pd.read_csv("megadataset.csv")


def content_extractor(content, start=None, end=None):
    try:
        if start and content and end:
            builder = "{}(.*)(?={})".format(start, end)
            pattern = re.compile(builder)
            return pattern.search(content).group(0)
        else:
            return content
    except Exception as e:
        return content


def tokenization_s(sentences):  # same can be achieved for words tokens
    s_new = []
    for sent in (sentences[:][0]):
        s_token = sent_tokenize(sent)
        if s_token != '':
            s_new.append(s_token)
    return s_new


def preprocess(text):
    clean_data = []
    for x in (text[:][0]):  # this is Df_pd for Df_np (text[:])
        new_text = re.sub('<.*?>', '', x)   # remove HTML tags
        new_text = re.sub(r'[^\w\s]', '', new_text)  # remove punc.
        new_text = re.sub(r'\d+', '', new_text)  # remove numbers
        new_text = new_text.lower()  # lower case, .upper() for upper
        if new_text != '':
            clean_data.append(new_text)
    return clean_data


def tokenization_w(words):
    w_new = []
    for w in (words[:][0]):  # for NumPy = words[:]
        w_token = word_tokenize(w)
        if w_token != '':
            w_new.append(w_token)
    return w_new


snowball = SnowballStemmer(language='english')


def stemming(words):
    new = []
    stem_words = [snowball.stem(x) for x in (words[:][0])]
    new.append(stem_words)
    return new


ser1 = df['text'].apply(
    lambda x: content_extractor(x, "start_text", "end_text"))
print(ser1)
test_pd = pd.DataFrame(ser1)
# text = pd.read_csv('twitter_text.csv', encoding='utf-8', header=None)
# clean_test = preprocess(test_pd)
# clean_words = tokenization_w(clean_test)
# stem_test = stemming(clean_words)


def text_process(text):
    '''
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Return the cleaned text as a list of words
    4. Remove words
    '''
    stemmer = WordNetLemmatizer()
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join([i for i in nopunc if not i.isdigit()])
    nopunc = [word.lower() for word in nopunc.split()
              if word not in stopwords.words('english')]
    return [stemmer.lemmatize(word) for word in nopunc]


#testing the function with a sample text#
sample_text = "Hey There! This is a Sample review, which 123happens {blah}%456 to contain happened punctuations universal rights of right contained."
for index, row in islice(test_pd.iterrows(), 0, None):
    new_entry = []
    new_entry += [text_process(str(row['text']))]
    processed_df = pd.DataFrame([new_entry], columns=['cleaned_text'])
    df = df.append(processed_df, ignore_index=True)

df.to_csv('preprocessed.csv', mode='w',
          columns=['cleaned_text'], index=False, encoding="utf-8")
