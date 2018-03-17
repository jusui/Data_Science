# coding: utf-8
"""
nlp_36.py

36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""
import MeCab
import ngram
from nlp_31 import *
from nlp_34 import *

def get_frequency(words: list) -> dict:
    """ リストに詰めた単語の頻度を辞書型で返す
    """
    frequency = {}
    for word in words:
        if frequency.get(word):
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency



if __name__ == '__main__':

    with open('neko.txt.mecab', encoding = 'utf-8') as file_wrapper:
        morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]
    # print(morphemes[::100])
    # print()

    frequency = get_frequency(morpheme['surface'] for morpheme in morphemes)

    # sort
    frequency = [ (k, v) for k, v in sorted(frequency.items(),
                                            key = lambda x: x[1], reverse = True) ]

    print("出現頻度Top.20 =\n", frequency[0:20])
