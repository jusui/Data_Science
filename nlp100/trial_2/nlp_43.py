# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import Morph
"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出

名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

class Chunk:
    
    def __init__(self, morphs: list, dst: str, srcs: str) -> None:
        """形態素(Morph object)のリスト(morphs), かかり先文節インデックス番号(dst),
        係り元文節インデックス番号のリスト(srcs)をメンバ変数に持つ"""

        self.morphs = morphs
        self.dst = int(dst.strip("D"))
        self.srcs = int(srcs)

    def join_morphs(self) -> str:
        """list morphs中の'記号'以外の各要素を結合して文字列を返す"""
        return ''.join([_morph.surface for _morph in self.morphs \
                        if _morph.pos != '記号'])

    def has_noun(self) -> bool:
        """any() : 引数内で指定した条件が少なからず一つ満たされている場合、Trueを返す。"""
        return any([_morph.pos == '名詞' for _morph in self.morphs])

    def has_verb(self) -> bool:
        return any([_morph.pos == '動詞' for _morph in self.morphs])

    def has_particle(self) -> bool:
        return any([_morph.pos == '助詞' for _morph in self.morphs])
    

    def pair(self, sentence: list) -> str:
        return self.join_morphs() + '\t' + sentence[self.dst].join_morphs()
        
    def __str__(self) -> str:
        return 'srcs: {}, dst: {}, morphs: ({})'\
            .format( self.srcs,
                     self.dst,
                     '/'.join([str(_morph) for _morph in self.morphs]) )

    
def make_chunk_list(analyzed_file_name: str) -> list:
    """係り受け解析済みの文章ファイルを読み込んで，
    各文をChunkオブジェクトのリストとして表現"""

    sentences = []
    sentence  = []
    _chunk = None
    with open(analyzed_file_name, encoding = 'utf-8') as input_file:
        for line in input_file:
            line_list = line.split()
            if line_list[0] == '*':
                if _chunk is not None:
                    sentence.append(_chunk)
                _chunk = Chunk(morphs = [], dst = line_list[2], srcs = line_list[1])

            elif line_list[0] == 'EOS': # End of sentence
                if _chunk is not None:
                    sentence.append(_chunk)
                if len(sentence) > 0:
                    sentences.append(sentence)
                _chunk = None
                sentence = []
                
            else:
                line_list = line_list[0].split(',') + line_list[1].split(',')
                _morph = Morph(surface = line_list[0], base = line_list[7],
                               pos = line_list[1], pos1 = line_list[2])
                _chunk.morphs.append(_morph)

    return sentences

def is_valid_chunk(_chunk, sentence):
    return _chunk.join_morphs() != '' and _chunk.dst > -1 \
                                   and sentence[_chunk.dst].join_morphs() != ''


if __name__ == '__main__':

    chunked_sentences = make_chunk_list('neko.txt.cabocha')

    for sentence in chunked_sentences:
        for chunk in sentence:
            if chunk.has_noun() and chunk.dst > -1 and sentence[chunk.dst].has_verb():
                print(chunk.pair(sentence))
