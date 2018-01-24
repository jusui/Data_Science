#coding: utf-8
"""
[MIT_DS:chap07]例外とアサーション

"""

def sumDigits(s):
    """
    [指練習7.1]
    s:string
    sの中から，数字の合計を返す. (e.f.) s = 'a2b3c' -> 5
    """

    sum = 0
    for char in string:
        try:
            sum += int(char)
        except ValueError: # Failure int(c)
            continue # pass
    return sum



def readInt(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg + ' ')
        try:
            val = int(val)
        except ValueError:
            print(str(val) + errorMsg)


def findEven(l):
    """
    [指練習7.2]
    l:list(int())
    lの中で最初に現れた偶数を返す
    lが偶数を含まなければ，ValueErrorを返す
    """
    for i in l:
        if i % 2 == 0:
            return i

    raise ValueError('findEven was called a list which has not integer.')


def getRatios(vec1, vec2):
    """
    vec1, vec2は同じ長さのlist
    vec1[i] / vec2[i] を意味する値からなるリストを返す
    """
    ratios = []
    for index in range(len(vec1)):
        try:
            ratios.append(vec1[index] / float(vec2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = Not a Number
        except:
            raise ValueError('getRations was called unexpected number')

    return ratios


def getRatios_2(vec1, vec2):
    """ 
    vec1, vec2: list
    vec1[i]/vec2[i]
    """
    ratios = []

    if len(vec1) != len(vec2):
        raise ValueError('Unexpected call in getRatios')
    for index in range(len(vec1)):
        vec1Elem = vec1[index]
        vec2Elem = vec2[index]
        if ( type(vec1Elem) not in (int, float)) or (type(vec2Elem) not in (int, float) ): # 要素は整数か小数
            raise ValueError('Unexpected call in getRatios')
        if vec2Elem == 0.0:
            ratios.append(float('NaN'))
        else:
            ratios.append(vec1Elem / vec2Elem)

    return ratios
        


def getGrades(fname):
    """
    try-exceptによるフロー制御

    """
    try:
        gradesFile = open(fname, 'r') # read file
    except IOError: # Could not file open
        raise ValueError('getGrade is Not open' + fname)
    grades = []

    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('行を小数に変換できません')
    return grades
      

    

if __name__ == '__main__':
    string = 'a2b3c'
    print(sumDigits(string))

    #    print(readInt())
    l = [1,2,4,5]
    print(findEven(l))


    vec1 = [1, 3, 4, 5]
    vec2 = [3, 4, 0.0, 10]
    print(getRatios(vec1, vec2))

    vec1 = [3, 4, 2, 10]    
    vec2 = [1, 2, 1, 5]
    print(getRatios_2(vec1, vec2))    
    
    
    try:
        grades = getGrades('quiz1grades.txt')
        grades.sort()
        median = grades[len(grades) % 2] # 2で割って小数点以下切り捨て
        print("成績の中央値 :", str(median))

    except ValueError:# errorMsg:
        print("Yeahhhhhhh", errorMsg)
