# -*- coding:utf8 -*-
"""
@Time    : 3/5/2022 6:04 PM

@Author  : Cgyhumble
"""

import sys
import string
import unicodedata
import pandas as pd
from gensim.parsing.preprocessing import STOPWORDS
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def keep_chr(ch):
    '''
    Find all characters that are classifed as punctuation in Unicode
    (except #, @, &) and combine them into a single string.
    '''
    return unicodedata.category(ch).startswith('P') and \
        (ch not in ("#", "@", "&"))

PUNCTUATION = " ".join([chr(i) for i in range(sys.maxunicode)
                        if keep_chr(chr(i))]) + string.punctuation

# When processing tweets, ignore these words
STOP_WORDS = ["a", "an", "the", "this", "that", "of", "for", "or",
              "and", "on", "to", "be", "if", "we", "you", "in", "is",
              "at", "it", "rt", "mt", "with"]

# When processing tweets, words w/ a prefix that appears in this list
# should be ignored.
STOP_PREFIXES = ("@", "#", "http", "&amp")

# combine more stop words
OTHER_WORDS = pd.read_fwf('../data/stopwords.txt', header=None).iloc[:, 0].tolist()

STOP_WORDS = list(set(STOP_WORDS).union(set(STOPWORDS)).union(set(ENGLISH_STOP_WORDS)).union(set(OTHER_WORDS)))
