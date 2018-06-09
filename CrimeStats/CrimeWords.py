import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


reader = csv.reader(open('/Users/leoniekruger/CencusData/Data/CrimeStats.csv', 'r',newline='\n'))
d = {}
for k,v in reader:
    d[k] = int(v)

#Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
#See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wordcloud = WordCloud(width=600,height=200, max_words=12,relative_scaling=1,margin=10).generate_from_frequencies(d)
default_colors = wordcloud.to_array()
#
# plt.figure( figsize=(20,10), facecolor='w')
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad=0)
# plt.show()


plt.title("Custom colors")
plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")

plt.imshow(wordcloud, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")
plt.show()