
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
print(word_counts)
"""Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 
 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
 """
top_three = word_counts.most_common(3)
print(top_three)
#输出 [('eyes', 8), ('the', 5), ('look', 4)]
morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))
#输出 [('eyes', 9), ('the', 5), ('look', 4)]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
#输出 [('eyes', 8), ('the', 5), ('look', 4)]

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))
#输出 [('eyes', 9), ('the', 5), ('look', 4)]


