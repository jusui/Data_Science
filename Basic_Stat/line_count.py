# coding: utf-8
import sys

"""
ファイル(quiz1grades.txt)の行数をカウントするスクリプト
[usage]
cat quiz1grades.txt | python egrep.py "[0-9]" | python line_count.py
"""

if __name__ == '__main__':
    count = 0

    for line in sys.stdin:
        count += 1

    # sys.stdoutに出力される
    print(count)
