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
""" 
[定義]より上の階層の型の属性を，定義なしに利用すること.
関連する抽象データ型をグループ化する仕組みを与える.
(e.f.)list(), str()はlen()が使える.

"""
class MITPerson(Person):
    """
    MITPerson classは，Person classのサブクラスであり，Personの属性を継承する
    サブクラスは，属性継承に加え，属性の追加・属性のオーバーライド(置換)が可能
    """

    nextIdNum = 0 # 個人識別番号

    def __init__(self, name):
        """ nextIdNumはMITPersonそのものに属すため，
        MITPersonのインスタンスが生成されるとき，nextIdNumの新たなインスタンスは生成されない """
        Person.__init__(self, name)        # 継承したインスタンスを初期化
        self.idNum = MITPerson.nextIdNum   # self.idNumを初期化
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum


    def isStudent(self):
        return isinstance(self, Student)

    
# [8.2.1]多重継承
class Student(MITPerson):
    pass # super classから継承する以外何も属性を持たないことを示す

class UG(Student): # under graduate
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(Student):
    # 学生の種類を区別
    pass # super classから継承する以外何も属性を持たないことを示す

class TransferStudent(Student):
    """ 編入生 """
    def init(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool


# [8.3.1]カプセル化と情報隠蔽
class Grades(object):
    """ list(講義登録学生), dict(個人番号:成績リスト) """
    
    def __init__(self):
        """ 空の成績ブックを生成する """
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """ studentをStudent型とする studentを成績ブックへ追加する"""
        if student in self.students:
            raise ValueError('Dupulicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """ float grade, gradeをstudentの成績リストへ追加 """
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """ studentの成績リストを返す """
        try: # studentの成績リストのコピーを返す
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
        
    def getStudents(self):
        """ 成績ブックに修められた学生んソートされたリストを返す """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True

        # 学生のリストのコピーを返すが，この方法は大規模データに対応できない
        # return self.students[:]
        for s in self.students:
            yield s # yield文があると，その関数がジェネレータであると判断される


            
# [8.3.2]情報隠蔽
class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'

    def printVisible(self):
        print(self.visible)

    def printInvisible(self):
        print(self.__invisible)

    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)


class subClass(infoHiding):
    def __init__(self):
        print('from subclass', self.__invisible)
        
    
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
    p1 = MITPerson('Barbara Beaver')
    print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))

    p1 = MITPerson('Mark Guttag')
    p2 = MITPerson('Billy Bob Beaver')
    p3 = MITPerson('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')

    print('p1 < p2 =', p1 < p2) # True
    print('p3 < p2 =', p3 < p2) # False
    print('p4 < p1 =', p4 < p1) # True

    
    p5 = Grad('Buzz Aldrin')      
    p6 = UG('Billy Beaver', 1984) # UG型のオブジェクトであり，Student型ではない!
    print(p5, 'is a graduate student is', type(p5) == Grad)
    print(p5, 'is an undergraduate student is', type(p5) == UG)

    print(p5, 'is a student is', p5.isStudent())
    print(p6, 'is a student is', p6.isStudent())
    print(p3, 'is a student is', p3.isStudent())

    # [8.3.1]
    def gradeReport(course):
        """ course(Grades型), 講義sixHundred に登録している学生の成績レポートを作成"""
        report = ''
        for s in course.getStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1

            try:
                average = tot/numGrades
                report = report + '\n'\
                         + str(s) + '\'s mean grade is ' + str(average)
            except ZeroDivisionError:
                report = report + '\n'\
                         + str(s) + ' has no grades'

        return report

    
    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)    
    ug3 = UG('David Henry', 2003)
    g1  = Grad('Billy Buckner')
    g2  = Grad('Bucky F. Dent')
    sixHundred = Grades()
    sixHundred.addStudent(ug1)
    sixHundred.addStudent(ug2)
    sixHundred.addStudent(g1)    
    sixHundred.addStudent(g2)    
    for s in sixHundred.getStudents():
        sixHundred.addGrade(s, 75)
    sixHundred.addGrade(g1, 25)
    sixHundred.addGrade(g2, 100)
    sixHundred.addStudent(ug3)
    print(gradeReport(sixHundred))

    # [8.3.2]
    test = infoHiding()
    print(test.visible)
    print(test.__alsoVisible__)
    ### AttributeError: 'infoHiding' object has no attribute '__invisible'
    # print(test.__invisible) 

    test = infoHiding()
    test.printInvisible()
    test.__printInvisible__()
    ### AttributeError: 'infoHiding' object has no attribute '__printInvisible'
    # test.__printInvisible() 

    ### AttributeError: 'subClass' object has no attribute '_subClass__invisible'
    # testSub = subClass() 
    

    # [8.3.3]
    book = Grades()
    book.addStudent(Grad('Julie'))
    book.addStudent(Grad('Charlie'))
    for s in book.getStudents():
        print(s)
