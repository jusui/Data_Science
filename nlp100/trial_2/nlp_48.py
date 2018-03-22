# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
from nlp_43 import *
"""
48. 名詞から根へのパスの抽出

文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．
*各文節は（表層形の）形態素列で表現する
*パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

def path_to_root(_chunk: Chunk, _sentence: list) -> list:
    """ 引数の文節(_chunk)がrootなら，その文節を返す.
    引数として与えられた文節(_chunk)がrootでないなら，
    その文節とその文節がかかっている文節からrootまでのパスをlistとして返す """

    if _chunk.dst == -1:
        return [_chunk]
    else:
        return [_chunk] + path_to_root(_sentence[_chunk.dst], _sentence)
    
def join_chunks_by_arrow(_chunks: list) -> None:
    return ' -> '.join([c.join_morphs() for c in _chunks])
    
def sorted_double_list(key_list: list, value_list: list) -> tuple:
    """ リストのキーと値を辞書にしてキーでソートして
    2につのリストに分解してタプルを返す """
    
    double_list = list(zip(key_list, value_list))
    double_list = dict(double_list)
    double_list = sorted(double_list.items())
    return [pair[0] for pair in double_list], [pair[1] for pair in double_list]

def save_sahen_case_frame_patterns(_sahen_case_frame_patterns: list,
                                   file_name: str) -> None:
    """ 動詞の格パターン(動詞と助詞の組み合わせ)のリストをファイルに保存 """

    with open(file_name, mode = 'w', encoding = 'utf-8') as output_file:
        for case in _sahen_case_frame_patterns:
            output_file.write('{}\t{}\t{}\n'.format(case[0],
                                                    ' '.join(case[1]),
                                                    ' '.join(case[2])))
    
if __name__ == '__main__':
    
    chunked_sentences = make_chunk_list('neko.txt.cabocha')
    for sentence in chunked_sentences[1:10]:
        for chunk in sentence:
            if chunk.has_noun():
                print(join_chunks_by_arrow(path_to_root(chunk, sentence)))
