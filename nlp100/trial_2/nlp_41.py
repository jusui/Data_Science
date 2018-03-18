# coding: utf-8
import CaboCha
import pydotplus
import subprocess
from nlp_40 import *
"""
41. 係り受け解析結果の読み込み（文節・係り受け）

40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
"""

class Chunk:
    
    def __init__(self, morphs: list, dst: str, srcs: str) -> None:
        """形態素(Morph object)のリスト(morphs), かかり先文節インデックス番号(dst),
        係り元文節インデックス番号のリスト(srcs)をメンバ変数に持つ"""

        self.morphs = morphs
        self.dst = int(dst.strip("D"))
        self.srcs = int(srcs)

    def __str__(self) -> str:
        return 'srcs: {}, dst: {}, morphs: ({})'\
            .format( self.srcs, self.dst,
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
                # Chunk() instance
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


if __name__ == '__main__':

    chunked_sentences = make_chunk_list('neko.txt.cabocha')

    for chunk in chunked_sentences[2]:
        print(str(chunk))
        
