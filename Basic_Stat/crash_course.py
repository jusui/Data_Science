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

# [2.1.12]set class
