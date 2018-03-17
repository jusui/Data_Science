# coding: utf-8
import CaboCha
import pydotplus
import subprocess
"""
nlp_40.py

40. 係り受け解析結果の読み込み（形態素）

形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

def make_analyzed_file(input_file_name: str, output_file_name: str) -> None:
    """cabocha fileを作る"""
    cbc = CaboCha.Parser()
    with open(input_file_name, encoding = 'utf-8') as input_file, \
         open(output_file_name, mode = 'w', encoding = 'utf-8') as output_file:

        for line in input_file:
            tree = cbc.parse(line.lstrip()) # 文字列の先頭の空白文字を除去
            output_file.write(tree.toString(CaboCha.FORMAT_LATTICE))


class Morph:
    """ 1つの形態素を表すクラス"""

    def __init__(self, surface, base, pos, pos1):

        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def is_end_of_sentence(self) -> bool:
        return self.pos1 == '句点'

    def __str__(self) -> str:
        return 'surface: {}, base: {}, pos: {}, pos1: {}'\
            .format(self.surface, self.base, self.pos, self.pos1)
    
def make_morph_list(analyzed_file_name: str) -> list:
    """係り受け解析したファイルを読み，Morphオブジェクトとして返す"""
        
    sentences = []
    sentence  = []
    with open(analyzed_file_name, encoding='utf-8') as input_file:
        
        for line in input_file:
            line_list = line.split()
            if (line_list[0] == '*') | (line_list[0] == 'EOS'):
                pass
            
            else:
                line_list = line_list[0].split(',') + line_list[1].split(',')
                # (e.f.)  ['見違える', '動詞', '自立', '*', '*', '一段',
                # '基本形', '見違える', 'ミチガエル', 'ミチガエル']

                _morph = Morph(surface = line_list[0], base = line_list[7],
                               pos = line_list[1], pos1 = line_list[2])

                sentence.append(_morph)

                if _morph.is_end_of_sentence():
                    sentences.append(sentence)
                    sentence = []
                    
    return sentences
        
        
        
if __name__ == '__main__':

    make_analyzed_file('neko.txt', 'neko.txt.cabocha')
    
    morphed_sentences = make_morph_list('neko.txt.cabocha') # 7486
    # print(len(morphed_sentences))

    for morph in morphed_sentences[2]:
        print(str(morph))

    
    
