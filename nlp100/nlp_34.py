# coding: utf-8
"""
nlp_34.py
usage: python nlp_34.py

34. 2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import MeCab
import ngram
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def tabbed_str_to_dict(tabbed_str: str) -> dict:
    """ tab区切りで形態素を表す文字列をdict型に変換"""

    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1],
                'pos': elements[2], 'pos1': elements[3]}

def morphemes_to_sentence(morphemes: list) -> list:
    """dict型で表された形態素のリストを句点毎にグルーピング，リスト化"""

    sentences = [] # append to sentence
    sentence  = [] # append to morpheme
    
    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []
            
    return sentences

def ngramed_list(lst: list, n: int = 3 ) -> list:
    """ listをNグラム化する: return ngramed list 
    lst: ngram化対称リスト
    n: integer N = 3 """
    
    index = ngram.NGram(N = n)
    return [term for term in index.ngrams(lst)]

def is_noun_no_noun(words: list) -> bool:
    """ 3単語で構成するリストが，「名詞―の―名詞」か判定
    words: [word1, word2, word3] """

    return (type(words) == list) and (len(words) == 3) and \
        (words[0]['pos1'].find('名詞') == 0) and \
        (words[1]['surface'] == 'の') and \
        (words[2]['pos1'].find('名詞') == 0)


if __name__ == '__main__':

    with open('neko.txt.mecab', encoding = 'utf-8') as file_wrapper:
        morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]

    # 「名詞―の―名詞」を含むngramのみ取り出す
    noun_no_noun = [ngrams for ngrams in ngramed_list(morphemes)
                    if is_noun_no_noun(ngrams)]
    print(noun_no_noun[::100])
    print()
    
    # 表層を取りだして結合
    noun_no_noun = [''.join([word['surface'] for word in ngram])
                    for ngram in noun_no_noun]
    
    print(noun_no_noun[::100]) # 情報過多なので，100step飛ばし
    
