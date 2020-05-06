import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import datetime
import matplotlib.dates as mdates
import nltk
from collections import Counter

stopwords = nltk.corpus.stopwords.words('english')
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))

df = pd.read_csv("https://raw.githubusercontent.com/shljessie/cds/master/final_csv/similaritycluster8.csv", error_bad_lines=False)


for i in range(8):
    print("Cluster ",i)
    clust = df[df['Cluster'] == i]
    words = (clust['Tweet']
           .str.lower()
           .replace([r'\|', RE_stopwords], [' ', ''], regex=True)
           .str.cat(sep=' ')
           .split()
    )

    # generate DF out of Counter
    rslt = pd.DataFrame(Counter(words).most_common(50), columns=['Word', 'Frequency']).set_index('Word')

    print(rslt)

print(df['Cluster'].value_counts())

# clust = df[df['Cluster'] == 2]
# words = (clust['Tweet']
#            .str.lower()
#            .replace([r'\|', RE_stopwords], [' ', ''], regex=True)
#            .str.cat(sep=' ')
#            .split()
# )

# # generate DF out of Counter
# rslt = pd.DataFrame(Counter(words).most_common(50), columns=['Word', 'Frequency']).set_index('Word')

# print(rslt)


#print(Counter(" ".join(clust["Tweet"]).split()).most_common(50))