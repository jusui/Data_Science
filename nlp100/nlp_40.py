# coding: utf-8
import CaboCha

"""
nlp_40.py

40. 係り受け解析結果の読み込み（形態素）

形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

def parse_neko():
    """ neko.txtを係り受け解析してneko.txt.cabochaに保存"""
    
    with open(fname) as data_file, open(fname_parsed, mode = 'w') as out_file:
        cabocha = CaboCha.Parser()
        for line in data_file:
            out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))
            # print(line)

class Morph:
    """ 形態素クラス
    表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）"""

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        """objectの文字列表現"""
        
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)

def neko_lines():
    """係り受け解析結果を読み込み，1文ずつMorph classのリストを返す"""

    with open(fname_parsed) as file_parsed:

        morphs = []
        for line in file_parsed:

            if line == 'EOS\n':
                yield morphs
                morphs = []

            else:
                # 先頭が*の行は係り受け解析結果なのでスキップ
                if line[0] == '*':
                    continue

                # 表層系はtab('\t')区切り，それ以外はコロン(',')区切り
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morphインスタンス作り，リストに作成Morph(surface, base, pos, pos1)
                morphs.append(Morph(cols[0], res_cols[6], res_cols[0], res_cols[1]))

        raise StopIteration
        
if __name__ == '__main__':

    fname = 'neko.txt'
    fname_parsed = 'neko.txt.cabocha'

    # 係り受け解析
    parse_neko()

    # 1文ずつリスト作成
    for i, morphs in enumerate(neko_lines(), 1):

        # 3文目を表示
        if i == 3:
            for morph in morphs:
                print(morph)
            break
        
