# from pylab import rcParams
import pandas as pd
from textblob import TextBlob
from itertools import islice
# import matplotlib.pyplot as plt
# import seaborn as sns
# import nltk
# from nltk.corpus import brown

df_data = pd.read_csv(
    "https://raw.githubusercontent.com/shljessie/cds/master/final_csv/us.csv")
# COLS = ['date', 'text', 'sentiment', 'subjectivity', 'polarity']
COLS = ['subjectivity', 'polarity']
df = pd.DataFrame(columns=COLS)

# Creating new csv:
for index, row in islice(df_data.iterrows(), 0, None):

    new_entry = []
    text = str(row['Text'])
    blob = TextBlob(text)
    sentiment = blob.sentiment

    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity

    # new_entry += [row['Date'], text, sentiment, subjectivity, polarity]
    new_entry += [subjectivity, polarity]

    single_survey_sentiment_df = pd.DataFrame([new_entry], columns=COLS)
    df = df.append(single_survey_sentiment_df, ignore_index=True)

df.to_csv('final_sub_pol.csv', mode='w',
          columns=COLS, index=False, encoding="utf-8")

# df.head()

# updated_df = pd.read_csv("data_sentiment.csv")
# # print(updated_df.describe())

# dffilter = updated_df.loc[(
#     updated_df.loc[:, updated_df.dtypes != object] != 0).any(1)]
# print(dffilter.describe())

# Histogram:
# plt.hist(dffilter['polarity'], color='darkred', edgecolor='black', density=False,
#          bins=int(30))
# plt.title('Polarity Distribution')
# plt.xlabel("Polarity")
# plt.ylabel("Number of TImes")

# rcParams['figure.figsize'] = 10, 15
# plt.show()

# Density curve:
# sns.distplot(dffilter['polarity'], hist=True, kde=True,
#              bins=int(30), color = 'darkred',
#              hist_kws={'edgecolor':'black'},axlabel ='Polarity')
# plt.title('Polarity Density')
# rcParams['figure.figsize'] = 10, 15
# plt.show()

# Frequent words:
# stopwords = nltk.corpus.stopwords.words('english')
# RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))
# words = (updated_df.text
#            .str.lower()
#            .replace([r'\|',r'\&',r'\-',r'\.',r'\,',r'\'', RE_stopwords], [' ', '','','','','',''], regex=True)
#            .str.cat(sep=' ')
#            .split()
# )
# from collections import Counter

# # generate DF out of Counter
# rslt = pd.DataFrame(Counter(words).most_common(10),
#                     columns=['Word', 'Frequency']).set_index('Word')
# print(rslt)
