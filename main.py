import feedparser
import util

COMMON_WORD_THRESHOLD = 5

url = 'http://feeds.nos.nl/nosnieuwseconomie'
feed = feedparser.parse(url)

#print(feed["entries"][0]["summary_detail"]["value"])

for i, entry in enumerate(feed["entries"]):
    util.create_wordcloud(util.remove_common_words(entry.summary, COMMON_WORD_THRESHOLD), "%s. %s" % (i, entry.title))
