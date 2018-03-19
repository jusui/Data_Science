# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
from nlp_42 import make_chunk_list, is_valid_chunk
from nlp_43 import Chunk
"""
44. 係り受け木の可視化

与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

def sentence_to_dot(idx: int, sentence: list) -> str:
    """dot言語作成の前処理[以下基本ルール]
    https://qiita.com/rubytomato@github/items/51779135bc4b77c8c20d """
    head = "digraph sentence{} ".format(idx)
    body_head = "{ graph [rankdir = LR]; "
    # 引数のアスタリスク:https://docs.python.jp/3/tutorial/controlflow.html#unpacking-argument-lists
    body_list = ['"{}"->"{}"; '.format(*chunk_pair.split()) for chunk_pair in sentence]

    return head + body_head + ''.join(body_list) + '}'

def sentences_to_dot(sentences: list ) -> list:
    """sentenceをdot言語に変換"""
    _dots = []
    for idx, sentence in enumerate(sentences):
        # print("sentence :", sentence)
        _dots.append(sentence_to_dot(idx, sentence))
    return _dots

def save_graph(dot: str, file_name: str) -> None:
    g = pydotplus.graph_from_dot_data(dot)
    g.write_jpeg(file_name, prog = 'dot')
    

if __name__ == '__main__':

    chunked_sentences = make_chunk_list('neko.txt.cabocha')
    paired_sentences = [ [chunk.pair(sentence) for chunk in sentence \
                          if is_valid_chunk(chunk, sentence)] \
                         for sentence in chunked_sentences \
                         if len(sentence) > 1 ]
    
    dots = sentences_to_dot(paired_sentences)

    for idx in range(101, 104):
      save_graph(dots[idx], 'graph{}.jpg'.format(idx))
      
