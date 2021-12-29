import pandas as pd
import re
from nltk.corpus import stopwords


def to_datetime(df: pd.DataFrame, dt_col: str, new_col: str, format: str = None):
    df[new_col] = pd.to_datetime(df[dt_col], format=format)


CLEANR = re.compile("<.*?>")


def normalize_text(string: str) -> str:
    no_html_string = re.sub(CLEANR, "", string)
    lower_string = no_html_string.lower()

    # remove numbers
    no_number_string = re.sub(r"\d+", "", lower_string)

    # remove all punctuation except words and space
    no_punc_string = re.sub(r"[^\w\s]", "", no_number_string)
    # as per recommendation from @freylis, compile once only
    # remove white spaces
    return no_punc_string.strip()


def remove_stopwords(string) -> str:
    stop_words_english = set(stopwords.words("english"))
    stop_words_spanish = set(stopwords.words("spanish"))
    # convert string to list of words
    lst_string = string.split()
    # remove stopwords
    no_stpwords_string = ""
    for i in lst_string:
        if not i in stop_words_english and not i in stop_words_spanish:
            no_stpwords_string += i + " "

    # removing last space
    return no_stpwords_string[:-1]
