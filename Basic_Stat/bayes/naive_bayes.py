# coding: utf-8
from collections import Counter, defaultdict
import sys, os
sys.path.append('/Users/usui/work/python/Data_Science/Basic_Stat/')
from machine_learning import split_data
import math, random, re, glob
from naiveBayes import readFiles, dataFrameFormDirectory

"""
[DS from scratch]12.Naive Bayes

[spam/ham dataset]
http://spamassassin.apache.org/old/publiccorpus/
"""

def tokensize(message):
    """文字を小文字に変換して単語を識別，重複を除く
    http://taustation.com/tag/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE/ """
    message = message.lower()
    # message(小文字)中の' (シングルコーテーション)を含むものを見つける
    all_words = re.findall("[a-z0-9']+", message) 
    return set(all_words)

def count_words(training_set):
    """学習データとしてラベル付けされたメッセージを数えて，
    単語をキーとする辞書を返す"""
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokensize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts
    
def word_probability(counts, total_spams, total_non_spams, k = 0.5):
    """数えたメッセージにスムージングを加えて確率を推定する
    word_counts => word, p(word|spam) and p(word|spam)"""
    return [ ( w,
               (spam + k) / (total_spam + 2 * k),
               (non_spam + k ) / (total_non_spam + 2 * k) )
             for w, (spam, non_spam) in counts.itmes() ]


def spam_probability(word_probs, message):
    """この確率とnaive bayesを用いてスパム確率:p_spam / (p_spam + p_not_spam)
    を見積もる"""
    message_word = tokensize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0 # Initialize

    # 語彙リストの単語を順に適用
    for word, prob_if_spam, prob_if_not_spam in word_probs:

        if word in message_probs: # += log(prob)
            log_prob_if_spam     += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)
        else: # += log(1.0 - prob)
            log_prob_if_spam     += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

    prob_if_spam     = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

class NaiveBayesClassifier:
    """分類器としてまとめる"""

    def __init__(self, k = 0.5):
        self.k = k
        self.word_probs = []
        
    def train(self, training_set):

        # count spam and Not spam mails
        num_spams = len( [is_spams
                          for message, is_spam in training_set
                          if is_spam] )
        num_not_spams = len(training_set) - num_spam

        word_counts = count_words(training_set)
        self.word_counts = word_probability(word_counts,
                                            num_spams,
                                            num_not_spams,
                                            self.k)

    def classify(self, message):
        return spam_probability(self.word_probs, message)


def get_subject_data(path):
    
    data = []
    
    return data
    
if __name__ == '__main__':
    
    path = '/Users/usui/work/python/jupyter_DataScience/emails/spam'
    data = data.append(dataFrameFormDirectory('/Users/usui/work/python/jupyter_DataScience/emails/spam', 'spam'))
    print(data)
