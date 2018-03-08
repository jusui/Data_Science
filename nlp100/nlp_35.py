# coding: utf-8
"""
nlp_35.py

35.名詞の連接（連続して出現する名詞）を最長一致で抽出せよ.
"""

import MeCab
import ngram
from nlp_31 import *
from nlp_34 import *

def morphemes_to_noun_array(morphemes: list) -> list:
    """ 辞書型の形態素リストを句点か名詞以外の形態素で区切ってグルーピングしリスト化
    morphemes: 辞書型の形態素リスト """

    nouns_list = []
    nouns = []

    for morpheme in morphemes:
        if morpheme['pos1'].find('名詞') >= 0:
            nouns.append(morpheme)
        elif (morpheme['pos1'] == '記号‐句点') | (morpheme['pos1'].find('名詞') < 0):
            nouns_list.append(nouns)
            nouns = []

    return [nouns for nouns in nouns_list if len(nouns) > 1]


if __name__ == '__main__':

    with open('neko.txt.mecab', encoding = 'utf-8') as file_wrapper:
        morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]
    # print(morphemes[::100])
    # print()

    noun_array = [ ''.join( [noun['surface'] for noun in nouns] )
                  for nouns in morphemes_to_noun_array(morphemes) ]
    
    print("連続して出現する名詞")
    print(noun_array[::100])
