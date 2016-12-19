from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt


def create_wordcloud(text,filenm):
    wc = WordCloud().generate(text)
    plt.figure(figsize=(18, 14))
    plt.imshow(wc)
    plt.savefig(filenm)


def remove_common_words(text, ranks_to_remove=25):
    top_words = Counter(text.split(" "))
    common = [t[0] for t in top_words.most_common(ranks_to_remove)]
    return " ".join([word for word in text.split(" ") if word not in common])


