# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
from nlp_43 import *
"""
45. 動詞の格パターンの抽出

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．
*動詞を含む文節において，最左の動詞の基本形を述語とする
*述語に係る助詞を格とする
*述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． 
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
*コーパス中で頻出する述語と格パターンの組み合わせ
*「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""

def case_patterns(_chunked_sentences: list) -> list:
    """ 動詞の格(case)のパターン(動詞と助詞の組み合わせ)のリストを返す
    base:形態素メンバ変数(基本形), dst:係り先文節インデックス番号
    srcs:係り元文節インデックス番号のリスト """
    
    _case_pattern = []
    for sentence in _chunked_sentences:
        for _chunk in sentence:
            if not _chunk.has_verb():
                continue
            # 助詞
            particles = [c.last_particle().base for c in sentence \
                         if c.dst == _chunk.srcs and c.has_particle()]

            if len(particles) > 0:
                _case_pattern.append([_chunk.first_verb().base, sorted(particles)]) # 動詞と助詞を格納

    return _case_pattern

def print_case_pattern_ranking(_grep_str: str) -> None:
    """コーパス中(case_pattern_txt)の出現頻度の高い順に上位20位をUNIXコマンドで表示する"""
    
    _grep_str = '' if _grep_str == '' else '| grep \'^{}\t\''.format(_grep_str)
    print( subprocess.run('cat case_patterns.txt {} | sort | uniq -c | sort -r | head -10'\
                         .format(_grep_str), shell = True) )

    
if __name__ == '__main__':
    
    chunked_sentences = make_chunk_list('neko.txt.cabocha')

    def save_case_patterns(_case_patterns: list, file_name: str) -> None:
        """動詞の格パターンのリストをファイル(case_patterns.txt)に保存"""
        
        with open(file_name, mode = 'w', encoding = 'utf-8') as output_file:
            for _case in _case_patterns:
                output_file.write('{}\t{}\n'.format(_case[0], ' '.join(_case[1])))

    save_case_patterns(case_patterns(chunked_sentences), 'case_patterns.txt')
    
    # UNIX commandで出現順に表示
    for grep_str in ['', 'する', '見る', '与える']:
        print_case_pattern_ranking(grep_str)
