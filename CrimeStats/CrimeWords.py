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

# Thanks https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py for the description/doc below
#
# """Word cloud object for generating and drawing.
#    Parameters
#    ----------
#    font_path : string
#        Font path to the font that will be used (OTF or TTF).
#        Defaults to DroidSansMono path on a Linux machine. If you are on
#        another OS or don't have this font, you need to adjust this path.
#    width : int (default=400)
#        Width of the canvas.
#    height : int (default=200)
#        Height of the canvas.
#    prefer_horizontal : float (default=0.90)
#        The ratio of times to try horizontal fitting as opposed to vertical.
#        If prefer_horizontal < 1, the algorithm will try rotating the word
#        if it doesn't fit. (There is currently no built-in way to get only
#        vertical words.)
#    mask : nd-array or None (default=None)
#        If not None, gives a binary mask on where to draw words. If mask is not
#        None, width and height will be ignored and the shape of mask will be
#        used instead. All white (#FF or #FFFFFF) entries will be considerd
#        "masked out" while other entries will be free to draw on. [This
#        changed in the most recent version!]
#    contour_width: float (default=0)
#        If mask is not None and contour_width > 0, draw the mask contour.
#    contour_color: color value (default="black")
#        Mask contour color.
#    scale : float (default=1)
#        Scaling between computation and drawing. For large word-cloud images,
#        using scale instead of larger canvas size is significantly faster, but
#        might lead to a coarser fit for the words.
#    min_font_size : int (default=4)
#        Smallest font size to use. Will stop when there is no more room in this
#        size.
#    font_step : int (default=1)
#        Step size for the font. font_step > 1 might speed up computation but
#        give a worse fit.
#    max_words : number (default=200)
#        The maximum number of words.
#    stopwords : set of strings or None
#        The words that will be eliminated. If None, the build-in STOPWORDS
#        list will be used.
#    background_color : color value (default="black")
#        Background color for the word cloud image.
#    max_font_size : int or None (default=None)
#        Maximum font size for the largest word. If None, height of the image is
#        used.
#    mode : string (default="RGB")
#        Transparent background will be generated when mode is "RGBA" and
#        background_color is None.
#    relative_scaling : float (default=.5)
#        Importance of relative word frequencies for font-size.  With
#        relative_scaling=0, only word-ranks are considered.  With
#        relative_scaling=1, a word that is twice as frequent will have twice
#        the size.  If you want to consider the word frequencies and not only
#        their rank, relative_scaling around .5 often looks good.
#        .. versionchanged: 2.0
#            Default is now 0.5.
#    color_func : callable, default=None
#        Callable with parameters word, font_size, position, orientation,
#        font_path, random_state that returns a PIL color for each word.
#        Overwrites "colormap".
#        See colormap for specifying a matplotlib colormap instead.
#    regexp : string or None (optional)
#        Regular expression to split the input text into tokens in process_text.
#        If None is specified, ``r"\w[\w']+"`` is used.
#    collocations : bool, default=True
#        Whether to include collocations (bigrams) of two words.
#        .. versionadded: 2.0
#    colormap : string or matplotlib colormap, default="viridis"
#        Matplotlib colormap to randomly draw colors from for each word.
#        Ignored if "color_func" is specified.
#        .. versionadded: 2.0
#    normalize_plurals : bool, default=True
#        Whether to remove trailing 's' from words. If True and a word
#        appears with and without a trailing 's', the one with trailing 's'
#        is removed and its counts are added to the version without
#        trailing 's' -- unless the word ends with 'ss'.
#    Attributes
#    ----------
#    ``words_`` : dict of string to float
#        Word tokens with associated frequency.
#        .. versionchanged: 2.0
#            ``words_`` is now a dictionary
#    ``layout_`` : list of tuples (string, int, (int, int), int, color))
#        Encodes the fitted word cloud. Encodes for each word the string, font
#        size, position, orientation and color.
#    Notes
#    -----
#    Larger canvases with make the code significantly slower. If you need a
#    large word cloud, try a lower canvas size, and set the scale parameter.
#    The algorithm might give more weight to the ranking of the words
#    than their actual frequencies, depending on the ``max_font_size`` and the
#    scaling heuristic.
