# coding: utf-8

"""
nlp_30.py
usage:python nlp_30.py

30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

[MeCab]
https://qiita.com/taroc/items/b9afd914432da08dafc8
"""
import MeCab

# [typing]文字列を受け取り文字列を返す関数とアノテーションを付ける
# https://docs.python.jp/3/library/typing.html
def make_analyzed_file(input_file_name: str, output_file_name: str) -> None:
    """文章ファイルを形態素解析してファイルに保存.
    :param input_file_name 日本語文章ファイル
    :param output_file_name 形態素解析済み文章ファイル"""
    
    _m = MeCab.Tagger("-Ochasen") # アンダースコアは内部だけで使用
    with open(input_file_name, encoding = 'utf-8') as input_file:
        with open(output_file_name, mode = 'w', encoding = 'utf-8') as output_file:
            output_file.write(_m.parse(input_file.read()))

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
    
    print("nlp_30")
    make_analyzed_file('neko.txt', 'neko.txt.mecab')

    with open('neko.txt.mecab', encoding = 'utf-8') as file_wrapper:
        morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]

    sentences = morphemes_to_sentence(morphemes)

    print(morphemes[::100])
    print(sentences[::100])
    print()

    verbs_surface = [morpheme['surface'] for morpheme in morphemes \
                     if morpheme['pos1'].find('動詞') == 0]
    
    verbs_base = [morpheme['base'] for morpheme in morphemes \
                     if morpheme['pos1'].find('動詞') == 0]

    verbs_suru = [morpheme['surface'] for morpheme in morphemes \
                     if morpheme['pos1'] == '名詞-サ変接続']
    print("nlp_31-32-33")
    print(verbs_surface[::100])
    print(verbs_base[::100])
    print(verbs_suru[::100])
    print()
    
