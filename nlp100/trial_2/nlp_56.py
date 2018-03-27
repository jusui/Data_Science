# coding: utf-8
"""
56. 共参照解析

Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現
（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

共参照:2つ以上の名詞が同一のものを指すこと.
(e.f)
「首相が初めて訪米した際、彼が歴史や文化に詳しいことを〜」
-> 「彼」＝「首相」と解析する処理
"""
from lxml import etree

tree = etree.parse("nlp.txt.xml")
rep_dict = {}

for coreference in tree.iterfind('./document/coreference/coreference'):
    # 代表参照表現の習得
    rep_text = coreference.findtext('./mention[@representative="true"]/text')

    # 代表参照表現以外のmention列挙，辞書に追加
    for mention in coreference.iterfind('./mention'):
        if mention.get('representative', 'false') == 'false':

            # 必要な情報の抽出
            sent_id = int(mention.findtext('sentence'))
            start   = int(mention.findtext('start'))
            end      = int(mention.findtext('end'))

            # 辞書に格納済の場合(=開始位置は同じだが終わりは違う)は先勝ち
            if not (sent_id, start) in rep_dict:
                rep_dict[(sent_id, start)] = (end, rep_text)

# 本文をrep_dictで置換し表示
for sentence in tree.iterfind('./document/sentences/sentence'):
    sent_id  = int(sentence.get('id'))  # sentence id
    org_rest = 0 # 置換中のtoken数の残り

    # token列挙
    for token in sentence.iterfind('./tokens/token'):
        token_id = int(token.get('id')) # token id

        # 置換対象
        if org_rest == 0 and (sent_id, token_id) in rep_dict:

            # 辞書から終了位置と代表参照表現を取り出し
            (end, rep_text) = rep_dict[(sent_id, token_id)]

            # 代表参照表現＋[ ]
            print('[' + rep_text + '] (', end='')
            org_rest = end - token_id # 置換中のtoken数の残り

        # token output
        print(token.findtext('word'), end='')

        # 置換終了なら閉じる
        if org_rest > 0:
            org_rest -= 1
            if org_rest == 0:
                print(')', end='')

        print(' ', end='')

    print() # sentence単位で改行
    
