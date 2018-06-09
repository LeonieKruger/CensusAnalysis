import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h = int(100.0 * float(random.randint(10, 100)) / 255.0)
    s = int(100.0 * 200.0 / 255.0)
    l = int(100.0 * 128.0 / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)

cmap=plt.get_cmap('ocean')
reader = csv.reader(open('/Users/leoniekruger/CencusData/Data/CrimeStats.csv', 'r',newline='\n'))
d = {}
for k,v in reader:
    d[k] = int(v)

wc = WordCloud(width=400,height=150,background_color="white", max_words=20, max_font_size=200, relative_scaling=0.3, prefer_horizontal=0.4 , random_state=42).generate_from_frequencies(d)

plt.imshow(wc.recolor(color_func=random_color_func, random_state=30))
plt.imshow(wc, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")
plt.show()