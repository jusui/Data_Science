# coding: utf-8
import sys, re

"""
grep スクリプト
[usage]
cat quiz1grades.txt | python egrep.py "[0-9]" | python line_count.py
"""

if __name__ == '__main__':
    # sys.argv：コマンドライン引数のリスト
    # sys.argv[0] : プログラム名
    # sys.argv[1] : コマンドライン上に指定した正規表現
    regex = sys.argv[1]

    # スクリプトが処理する各行に対して
    for line in sys.stdin:
        # 正規表現に合致したら，stdoutに出力する
        if re.search(regex, line):
            sys.stdout.write(line)
