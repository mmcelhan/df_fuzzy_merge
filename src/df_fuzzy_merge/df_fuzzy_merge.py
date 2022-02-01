import pandas as pd
import fuzzywuzzy
from fuzzywuzzy import process
import nltk
from nltk.corpus import stopwords

if not list(set(stopwords.words('english'))):
    nltk.download('stopwords')


def df_fuzzy_merge(df_1, df_2, left_on, right_on, threshold=80, limit=1, fm_stopwords="", how="inner"):
    """
    :param df_1-pandas dataframe, is the left table to join
    :param df_2-pandas dataframe, is the right table to join
    :param left_on-list, is the key column or columns of the left table
    :param right_on-list, is the key column or columns of the right table
    :param threshold-int 0 to 100, is how close the matches should be to return a match, based on Levenshtein distance
    :param limit- int, minimum 1 is the amount of matches that will get returned, these are sorted high to low
    :param fm_stopwords-list, input list of stopwords. defaults to the nltk english stopwords list
    :param how, defaults to inner as inner join. Can be selected to be left as well
    :return: returns the joined dataframe

    This function calls an inner join with df_1 and df_2 using fuzzy logic on the columns described to match
    Only rows that match in both dataframes are returned
    """
    pass

    # create null match columns
    df_1['match_key'] = ''
    df_2['match_key'] = ''
    if fm_stopwords == "":
        # if no stop words are given, use the nltk stop word corpus
        fm_stopwords = return_stop_words()

    # combines the list of column inputs into a single string for matching
    for value in left_on:
        df_1['match_key'] = df_1['match_key'].map(str) + ' ' + df_1[value].map(str)

    for value in right_on:
        df_2['match_key'] = df_2['match_key'].map(str) + ' ' + df_2[value].map(str)

    # remove periods for abbreviated names
    df_1['match_key'] = df_1['match_key'].map(lambda x: x.strip(".,!"))
    df_2['match_key'] = df_2['match_key'].map(lambda x: x.strip(".,!"))

    # applies lower case and removes common words like "college" and "the"
    df_1['match_key'] = df_1['match_key'].apply(format_match_string, args=(fm_stopwords,))
    df_2['match_key'] = df_2['match_key'].apply(format_match_string, args=(fm_stopwords,))

    # the match process-creates the match keys to a list, matches, then saves them in the match column
    s = df_2['match_key'].tolist()
    m = df_1['match_key'].apply(lambda x:
                                process.extract(x, s, limit=limit, scorer=fuzzywuzzy.fuzz.token_sort_ratio))
    df_1['match'] = m

    # drop the score value and only keep the match words
    m2 = df_1['match'].apply(lambda x: ', '.join([i[0] for i in x if i[1] >= threshold]))
    df_1['match'] = m2

    # merge based on the matches, suffixes to drop the columns later
    df_1 = df_1.merge(df_2, how=how, left_on='match', right_on='match_key', suffixes=['', '_y'])

    # drop the matching name columns since this is a left join
    df_1 = df_1[df_1.columns.drop(list(df_1.filter(regex='_y')))]
    df_1 = df_1[df_1.columns.drop(['match_key', 'match'])]
    return df_1


def format_match_string(string, fm_stopwords):
    """ function that converts to lower case and removes stop words """
    string = string.lower().split()
    string = [word for word in string if word not in fm_stopwords]  # remove stop words
    string = ' '.join(string)
    return string


def return_stop_words():
    """ function that returns stopwords using nltk's library """
    english_stopwords = list(set(stopwords.words('english')))
    return english_stopwords

