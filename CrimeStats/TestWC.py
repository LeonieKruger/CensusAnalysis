from PIL import Image
from PIL import ImageFilter
from wordcloud import WordCloud
import csv
import numpy as np


def draw_contour(img, mask, contour_width, contour_color):
    """Draw mask contour on a pillow image."""
    contour = Image.fromarray(mask)
    contour = contour.resize(img.size)
    contour = contour.filter(ImageFilter.FIND_EDGES)
    contour = np.array(contour)

    # make sure borders are not drawn
    contour[[0, -1], :] = 0
    contour[:, [0, -1]] = 0

    # use a gaussian to define the contour width
    radius = contour_width / 10
    contour = Image.fromarray(contour)
    contour = contour.filter(ImageFilter.GaussianBlur(radius=radius))
    contour = np.array(contour) > 0
    contour = np.dstack((contour, contour, contour))

    # color the contour
    ret = np.array(img) * np.invert(contour)
    if contour_color != 'black':
        color = Image.new(img.mode, img.size, contour_color)
        ret += np.array(color) * contour

    return Image.fromarray(ret)

reader = csv.reader(open('/Users/leoniekruger/CencusData/Data/CrimeStats.csv', 'r',newline='\n'))
d = {}
for k,v in reader:
    d[k] = int(v)

mask = np.array(Image.open("/Users/leoniekruger/Downloads/crying_female_silhouette.png"))
#Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
#See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wc = WordCloud(max_words=12,relative_scaling=1, mask=mask,).generate_from_frequencies(d)
contour = draw_contour(wc.to_image(), wc.mask, 1, 'blue')
contour.show()