# coding: utf-8
"""
nlp100
nlp_08.py

暗号文

    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

        英小文字ならば(219 - 文字コード)の文字に置換
        その他の文字はそのまま出力

    この関数を用い，英語のメッセージを暗号化・復号化せよ．

"""
import re

def cipher(text):
    # re.sub() でtext 内に存在する, 条件lambdaに該当する部分だけ置換
    # m.group(0), は正規表現の一種で完全一致
    # http://uxmilk.jp/8662
    return re.sub(r"[a-z]", lambda m: chr(219 - ord(m.group(0))), text)


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor" \
            " incididunt ut labore et dolore magna aliqua."

encrypt = cipher(text)
print("Encryption:", encrypt)

decrypt = cipher(encrypt)
print("decrypt:", decrypt)
