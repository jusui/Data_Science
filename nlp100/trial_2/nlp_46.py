# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
from nlp_43 import *
from nlp_45 import *
"""
46. 動詞の格フレーム情報の抽出

45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．
 *項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
 *述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を
"""

def sorted_double_list(key_list: list, value_list: list) -> tuple:
    """ リストのキーと値を辞書にしてキーでソートして
    2につのリストに分解してタプルを返す """
    
    double_list = list(zip(key_list, value_list))
    double_list = dict(double_list)
    double_list = sorted(double_list.items())
    return [pair[0] for pair in double_list], [pair[1] for pair in double_list]
    
def case_frame_patterns(_chunked_sentences: list) -> list:
    """ 動詞の格フレームのパターン(動詞と助詞の組み合わせ)のリストを返す """
    
    _case_frame_patterns = []
    for sentence in _chunked_sentences:
        for _chunk in sentence:
            if not _chunk.has_verb():
                continue

            clauses = [c.join_morphs() for c in sentence \
                       if c.dst == _chunk.srcs and c.has_particle()]

            particles = [c.last_particle().base for c in sentence \
                         if c.dst == _chunk.srcs and c.has_particle()]

            if len(particles) > 0: # base:基本形
                _case_frame_patterns.append([_chunk.first_verb().base,
                                             *sorted_double_list(particles, clauses)])

    return _case_frame_patterns

def save_case_frame_patterns(_case_frame_patterns: list, file_name: str) -> None:
    """ 動詞の格パターン(動詞と助詞の組み合わせ)のリストをファイルに保存 """

    with open(file_name, mode = 'w', encoding = 'utf-8') as output_file:
        for case in _case_frame_patterns:
            output_file.write('{}\t{}\t{}\n'.format(case[0], ' '.join(case[1]), ' '.join(case[2])))
            
def print_case_pattern_ranking(_grep_str: str) -> None:
    """コーパス中(case_pattern_txt)の出現頻度の高い順に上位20位をUNIXコマンドで表示する"""
    
    _grep_str = '' if _grep_str == '' else '| grep \'^{}\t\''.format(_grep_str)
    print( subprocess.run('cat case_frame_patterns.txt {} | sort | uniq -c | sort -r | head -10'\
                         .format(_grep_str), shell = True) )

    
if __name__ == '__main__':
    
    chunked_sentences = make_chunk_list('neko.txt.cabocha')
    save_case_frame_patterns(case_frame_patterns(chunked_sentences), 'case_frame_patterns.txt')
    
    # UNIX commandで出現順に表示
    for grep_str in ['', 'する', '見る', '与える']:
        print_case_pattern_ranking(grep_str)
