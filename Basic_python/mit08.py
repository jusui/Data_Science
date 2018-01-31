# coding: utf-8
"""
[MIT_DS:chap08]抽象データ型とクラス

"""

# [8.1.1]
class IntSet(object):
    """ 
    intSetは整数の集合である 
    集合は，int型の要素からなるリストself.vals
    int型の要素はそれぞれ，リストself.valsにちょうど一度だけ現れる
    """
    
    def __init__(self):
        """ 
        整数の空集合を生成
        クラスをインスタンス化する度に，呼び出される
        """
        self.vals = []

    def insert(self, e):
        """ int e, eをselfに挿入 """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ int e, eがselfにあればTrue, なければFalse """
        return e in self.vals

    def remove(self, e):
        """ int e, eをselfから削除，selfになければValueError """
        try:
            self.vals.remove(e)
        except:
            raise ValueError( str(e) + ' not found' )

    def getMembers(self):
        """ selfが含む要素を持つリストを返す, 要素の順序を指定できない """
        return self.vals[:]

    def __str__(self):
        """ 
        selfの文字列表現を返す
        print()が起動するとき，オブジェクトに関連付けられた__str__関数が自動的に呼ばれる
        """
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'      # [:-1]で最後のカンマを除く


    
import datetime
# [8.1.2]
class Person(object):
    """ 
    (e.f)大学の学生，教員データ管理
    学生:姓，名，住所，学年，成績
    教員:姓，名，住所，学年，成績，給与，履歴

    学生と教員の共通点->「人間」->class Person
    
    """
    def __init__(self, name):
        """ 「人間」を生成する """
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lasBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getName(self):
        """ selfの名前を返す """
        return self.name

    def getLastName(self):
        """ selfの姓を返す """
        return self.lastName

    def setBirthday(self, birthdate):
        """ birthdate をdatetime.date型とする
        selfの生年月日をbirthdateと設定 """
        self.birthday = birthdate
    
    def getAge(self):
        """ selfの現在の年齢を日単位で返す """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """ selfの名前がotherの名前と比べてアルファベット順で前ならばTrue, 
        それ以外はFalseを返す．
        比較は，姓について行うが，姓が同じ場合は名前で比較する"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """ selfの名前を返す """
        return self.name


# [8.2] 継承(inheritance)

    

if __name__ == '__main__':
    # [8.1.1]class IntSet
    s = IntSet()  # instance
    s.insert(3)   # "." : attribute reference
    print(s.member(3))
    s.insert(4)
    print(s)

    
    # [8.1.2]class Person
    me  = Person('Michael Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    print(him.getLastName())
    him.setBirthday(datetime.date(1961, 8, 4))
    her.setBirthday(datetime.date(1958, 8, 16))
    print(him.getName(), 'is', him.getAge(), 'days old')

    pList = [me, him, her]
    for p in pList:
        print(p)
        
    pList.sort()
    for p in pList:
        print(p)


    # [8.2]
