# coding: utf-8
"""
nlp_31, 32, 33
usage:python nlp_31.py

31. 動詞の表層形をすべて抽出せよ．
"""

import MeCab
import ngram
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# from nlp_30 import tabbed_str_to_dict, morphemes_to_sentence

def tabbed_str_to_dict(tabbed_str: str) -> dict:
    """タブ区切りで形態素を表す文字列をdict型に変換する.
    :param  tabbed_str tab区切りで形態素を表す文字列
    :param dict型の形態素 """

    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1],
                'pos': elements[2], 'pos1': elements[3]}

def morphemes_to_sentence(mrophemes: list) -> list:
    """dict型で表された形態素のリストを句点毎にグルーピング，リスト化．
    :param morphemes(形態素) dict型で表された形態素リスト
    :return 文章リスト"""
    
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []
            
    return sentences

if __name__ == '__main__':
    with open('neko.txt.mecab', encoding = 'utf-8') as file_wrapper:
        morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]
        
    sentences = morphemes_to_sentence(morphemes)

    verbs_surface = [morpheme['surface'] for morpheme in morphemes \
                     if morpheme['pos1'].find('動詞') == 0]
    
    verbs_base = [morpheme['base'] for morpheme in morphemes \
                     if morpheme['pos1'].find('動詞') == 0]

    verbs_suru = [morpheme['surface'] for morpheme in morphemes \
                     if morpheme['pos1'] == '名詞-サ変接続']

    print("情報過多なので，100step飛ばしで表示")
    print(verbs_surface[::100])
    print(verbs_base[::100])
    print(verbs_suru[::100])
