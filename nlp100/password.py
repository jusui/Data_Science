# coding : utf-8

import re

def solution(S):
    result = -1;
    list = re.split('[0-9]', S)
    for cand in list:
        if not cand.islower(): # islower():小文字判定
            tmp = len(cand)
            if tmp > result:
                result = tmp
    return result
    

if __name__ == '__main__':

    str1 = "a0bb"
    str2 = "aBa"

    print(solution(str1))
    print(solution(str2))
