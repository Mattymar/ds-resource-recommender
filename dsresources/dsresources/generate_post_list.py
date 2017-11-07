import feedparser


## TODO: Add way to add and remove feeds from list

feeds = ['http://www.erogol.com/feed/',
        'http://logicx24.github.io/feed.xml',
        'https://adeshpande3.github.io/adeshpande3.github.io/feed.xml',
        'http://advanceddataanalytics.net/feed/',
        'http://blog.smola.org/rss',
        'http://blog.sense.io/rss/',
        'https://medium.com/feed/@D33B',
        'https://medium.com/feed/airbnb-engineering']


## TODO: Add filter to return links for posts after a certain date


def get_posts_from_feed_list(feed_list):
    posts = []
    for feed in feed_list:
        # print('*******FEED******')
        # print(feed)
        d = feedparser.parse(feed)
        for entry in d.entries:
            posts.append({'url': entry.links[0].href, 'title': entry.title, 'pub_date': entry.published})
    return posts



#print(get_posts_from_feed_list(feeds))