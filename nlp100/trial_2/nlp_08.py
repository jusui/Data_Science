# coding: utf-8
"""
8.暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
import re

def cipher(sentence):
    return re.sub(r"[a-z]", lambda m: chr(219 - ord(m.group(0))), sentence)

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor" " incididunt ut labore et dolore magna aliqua."

encrypt = cipher(sentence)
print("Encryption:", encrypt)
decrypt = cipher(encrypt)
print("decrypt :", decrypt)
