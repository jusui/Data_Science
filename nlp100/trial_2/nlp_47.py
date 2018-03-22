# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
from nlp_43 import *
"""
47. 機能動詞構文のマイニング

動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ
*「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
*述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
*述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
*述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．
返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
*コーパス中で頻出する述語（サ変接続名詞+を+動詞）
*コーパス中で頻出する述語と助詞パターン
"""

def sahen_case_frame_patterns(_chunked_sentences: list) -> list:
    """ 動詞の格フレームのパターン(動詞と助詞の組み合わせ)のリストを返す """

    _sahen_case_frame_patterns = []
    for sentence in _chunked_sentences:
        for _chunk in sentence:
            if not _chunk.has_verb():
                continue

            sahen_connection_noun = [c.join_morphs() for c in sentence if c.dst == _chunk.srcs \
                                     and c.has_sahen_connection_noun_plus_wo()]
            clauses = [c.join_morphs() for c in sentence if c.dst == _chunk.srcs \
                       and not c.has_sahen_connection_noun_plus_wo() \
                       and c.has_particle()]

            particles = [c.last_particle().base for c in sentence \
                         if c.dst == _chunk.srcs \
                         and not c.has_sahen_connection_noun_plus_wo() \
                         and c.has_particle()]

            if len(sahen_connection_noun) > 0 and len(particles) > 0:
                _sahen_case_frame_patterns.append(
                    [sahen_connection_noun[0] + _chunk.first_verb().base,
                     *sorted_double_list(particles, clauses)]
                )

    return _sahen_case_frame_patterns
    
def sorted_double_list(key_list: list, value_list: list) -> tuple:
    """ リストのキーと値を辞書にしてキーでソートして
    2につのリストに分解してタプルを返す """
    
    double_list = list(zip(key_list, value_list))
    double_list = dict(double_list)
    double_list = sorted(double_list.items())
    return [pair[0] for pair in double_list], [pair[1] for pair in double_list]
    
# def case_frame_patterns(_chunked_sentences: list) -> list:
#     """ 動詞の格フレームのパターン(動詞と助詞の組み合わせ)のリストを返す """
    
#     _case_frame_patterns = []
#     for sentence in _chunked_sentences:
#         for _chunk in sentence:
#             if not _chunk.has_verb():
#                 continue

#             clauses = [c.join_morphs() for c in sentence \
#                        if c.dst == _chunk.srcs and c.has_particle()]

#             particles = [c.last_particle().base for c in sentence \
#                          if c.dst == _chunk.srcs and c.has_particle()]

#             if len(particles) > 0: # base:基本形
#                 _case_frame_patterns.append([_chunk.first_verb().base,
#                                              *sorted_double_list(particles, clauses)])

#     return _case_frame_patterns

def save_sahen_case_frame_patterns(_sahen_case_frame_patterns: list,
                                   file_name: str) -> None:
    """ 動詞の格パターン(動詞と助詞の組み合わせ)のリストをファイルに保存 """

    with open(file_name, mode = 'w', encoding = 'utf-8') as output_file:
        for case in _sahen_case_frame_patterns:
            output_file.write('{}\t{}\t{}\n'.format(case[0],
                                                    ' '.join(case[1]),
                                                    ' '.join(case[2])))
            
# def print_case_pattern_ranking(_grep_str: str) -> None:
#     """コーパス中(case_pattern_txt)の出現頻度の高い順に上位20位を
#     UNIXコマンドで表示する"""
    
#     _grep_str = '' if _grep_str == '' else '| grep \'^{}\t\''.format(_grep_str)
#     print( subprocess.run('cat case_frame_patterns.txt {} | \
#     sort | uniq -c | sort -r | head -10'\
#                           .format(_grep_str), shell = True) )

    
if __name__ == '__main__':
    
    chunked_sentences = make_chunk_list('neko.txt.cabocha')
    save_sahen_case_frame_patterns(sahen_case_frame_patterns(chunked_sentences),
                                   'sahen_case_frame_patterns.txt')

    # コーパス中で頻出する述語(サ変接続名詞+ を+動詞)をUNIXで確認
    print(subprocess.run('cat sahen_case_frame_patterns.txt \
    | cut -f 1 | sort | uniq -c | sort -r | head -10', shell = True))

    # コーパス中で頻出する述語と助詞をUNIXで確認
    print(subprocess.run('cat sahen_case_frame_patterns.txt \
    | cut -f 1,2 | sort | uniq -c | sort -r | head -10', shell = True))
