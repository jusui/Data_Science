# coding: utf-8

score_list = []

score_list_file = open("./score.txt")

for score in score_list_file:
    # back slushの削除, 行末の文字列を削除rstrip(), カンマでsplit(",")
    score = score.rstrip().split(",")

    # 1番目は，文字列をint型にしてappend( [ score[0], int(score[1]) ] )
    score_list.append( [ score[0], int(score[1]) ] )
# 開いたファイルは必ず閉じる
score_list_file.close()

print(score_list)
    
