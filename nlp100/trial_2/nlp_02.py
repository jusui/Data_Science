# coding: utf-8
"""
2.「パトカー」＋「タクシー」の文字を先頭から交互に連結して
文字列「パタトクカシーー」を得よ
"""
sentence1 = "パトカー"
sentence2 = "タクシー"
print(''.join([a + b for a, b in zip(sentence1, sentence2)]))
