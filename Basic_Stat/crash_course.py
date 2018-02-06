#coding: utf-8
import re
from collections import defaultdict, Counter
"""
[DS from scratch]
chap.2
Crash Course in Python3
Python速習



"""

my_regax = re.compile("[0-9]+", re.I)
lookup = defaultdict(int)
my_counter = Counter()
match = 10
print(match)


# [2.1.11.1] defaultdict class
""" 文章中の単語の出現数をカウントする """
document = "asldkjfoqwiretlanglk"

# case.1
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
# case.2
word_counts_2 = {}        
for word in document:
    try:
        word_counts_2[word] += 1
    except:
        word_counts_2[word] = 1
# case.3
word_counts_3 = {}
for word in document:
    previous_count = word_counts_3.get(word, 0)
    word_counts_3[word] = previous_count + 1

#
word_counts = defaultdict(int) # int()
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seatle"
print(dd_dict)

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1
print(dd_pair)

# [2.1.11.2]Counter class
c = Counter([0, 1, 2, 3]) # Counter({0: 1, 1: 1, 2: 1, 3: 1})
print("c :", c)


document2 = "irohanihotetochirinuruwo"
word_counts = Counter(document2)

# 出現数ベスト10
for word, count in word_counts.most_common(10):
    print(word, count)
print()
   
# [2.1.12]set class
print("集合")
s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s) 
print(x) # 2
y = 2 in s
print(y) # True
z = 3 in s
print(z) # False
hundreds_of_other_words = ["asdfl","asldjf", "alretk"]
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
print("zip" in stopwords_list) # False

stopwords_set = set(stopwords_list)
print("zip" in stopwords_set) # False

""" リストの重複を削除して再度リスト化する """
item_list = [1, 2, 3, 1, 2, 3]
num_item = len(item_list)
print(num_item) # 6
item_set = set(item_list)
print(item_set) # {1, 2, 3}

num_distinct_items = len(item_set)
print(num_distinct_items) # 3
distinct_item_list = list(item_set)
print(distinct_item_list) # [1, 2, 3]

# [2.1.13]実行順制御
if 1 > 2:
    message = "if 1 > 2"
elif 1 > 3:
    message = "elif means else if"
else:
    message = "すべての条件に該当しない場合，else->exe"

parity = "even" if x % 2 == 0 else "odd"

x = 0
while x < 10:
    print(x, "is smaller than 10.")
    x += 1

for x in range(10):
    print(x, "is smaller than 10")

for x in range(10):
    if x == 3:
        continue # 実行中のループ先頭に戻り，処理を継続
    if x == 5:
        break # ループを脱出
    print(x) # 0, 1, 2, 4


# [2.1.14]真偽
print("[2.1.14]真偽")
one_is_less_than_tow = 1 < 2 # 代入される値はTrue
true_equals_false = True == False # 代入される値はFalse

x = None
print(x == None) # True が表示されるが，Python的ではない
print(x is None) # Trueが表示される，Python的なコード



