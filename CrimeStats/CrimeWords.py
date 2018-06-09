import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(10, 50)


reader = csv.reader(open('/Users/leoniekruger/CencusData/Data/CrimeStats.csv', 'r',newline='\n'))
d = {}
for k,v in reader:
    d[k] = int(v)

wc = WordCloud(width=600,height=150,background_color="white", max_words=20, max_font_size=200, relative_scaling=0.5, prefer_horizontal=0.4 , random_state=42).generate_from_frequencies(d)

wc.recolor(color_func=grey_color_func, random_state=3)
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))

plt.imshow(wc, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")
plt.show()