# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
from nlp_43 import *
"""
49. 名詞間の係り受けパスの抽出

文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
*問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
*文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．
*文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
*上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
"""
def noun_pairs(_sentence: list):
    """
    引数として渡された文章が持つ全ての名詞節から作ることが出来る全てのペアのリストを返す
    """

    from itertools import combinations
    _noun_chunks = [_chunk for _chunk in _sentence if _chunk.has_noun()]
    return list(combinations(_noun_chunks, 2))

def common_chunk(path_i: list, path_j: list) -> Chunk:
    """文節iと文節jから構文木の木に至る経路上で共通の文節kで交わる場合，文節kを返す"""

    _chunk_k = None
    path_i = list(reversed(path_i))
    path_j = list(reversed(path_j))
    for idx, (c_i, c_j) in enumerate(zip(path_i, path_j)):
        if c_i.srcs != c_j.srcs:
            _chunk_k = path_i[idx - 1]
            break
        
    return _chunk_k
    
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

    for sentence in chunked_sentences:
        # 名詞句のペアのリスト
        n_pairs = noun_pairs(sentence)
        if len(n_pairs) == 0:
            continue

        for n_pair in n_pairs:
            chunk_i, chunk_j = n_pair

            # 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
            chunk_i.replace_noun('X')
            chunk_j.replace_noun('Y')

            # 文節iとjからrootへのパス(Chunk型のリスト)
            path_chunk_i_to_root = path_to_root(chunk_i, sentence)
            path_chunk_j_to_root = path_to_root(chunk_j, sentence)

            if chunk_j in path_chunk_i_to_root:
                # 文節iから構文木の根に至る経路上に分節jが存在する場合

                # 文節jの文節iから構文木の根に至る経路上におけるインデックス
                idx_j = path_chunk_i_to_root.index(chunk_j)

                # 文節iから分節jのパスを表示
                print(join_chunks_by_arrow(path_chunk_i_to_root[0: idx_j + 1]))
            else:
                # 上記以外で，文節iと文節jから構文木の根に至る経路上で
                # 共通の分節kで交わる場合

                # 文節kを習得
                chunk_k = common_chunk(path_chunk_i_to_root, path_chunk_j_to_root)

                if chunk_k is None:
                    continue
                
                # 文節kの文節iから構文木の根に至る経路上におけるインデックス
                idx_k_i = path_chunk_i_to_root.index(chunk_k)

                # 文節kの文節jから構文木の根に至る経路上におけるインデックス
                idx_k_j = path_chunk_j_to_root.index(chunk_k)
                
                # 文節iから文節kに至る直前のパスと分節jから分節kに至る直前までのパス，
                # 文節kの内容をパイプ"|"で連結して表示
                print(' | '\
                      .join(
                          [ join_chunks_by_arrow(path_chunk_i_to_root[0: idx_k_i]),
                            join_chunks_by_arrow(path_chunk_j_to_root[0: idx_k_j]),
                            chunk_k.join_morphs() ]
                      )
                )
