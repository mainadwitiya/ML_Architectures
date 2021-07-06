import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
import re
df =pd.read_csv('train.csv')

def remove_lower_case(df,column_name_text,new_col_name):
    #lowercase
    df[new_col_name] = df[column_name_text].str.lower()
    
    


def remove_punctuation(column_name_text):
    PUNCT_TO_REMOVE = string.punctuation
    #Usage df[column_name_text] = df[column_name_text].apply(lambda text: remove_punctuation(text))
    return column_name_text.translate(str.maketrans('','',PUNCT_TO_REMOVE))


def remove_stopwords(column_name_text):
    stopwords_list = set(stopwords.words('english'))
    #Usage df["column_name_text"] = df["column_name_text"].apply(lambda text: remove_stopwords(text))
    return " ".join([word for word in str(column_name_text).split() if word not in stopwords_list])
    

# remove very frequent words
def remove_html_tags(string):
    result=re.sub('<.*?>','',string)
    return result
    '''Usage 
    df['text']=df['text'].apply(lambda x: remove_html_tags(x))
    '''
