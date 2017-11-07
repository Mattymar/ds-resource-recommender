import requests
from readability import Document
import html2text
import feedparser
import listparser
# import generate_post_list


# response = requests.get('https://github.com/HFTrader/DeepLearningBook/blob/master/files/Chap6.pdf')
# doc = Document(response.text)
# text = html2text.html2text(doc.summary())
# print(text)
# posts = get_posts_from_feed_list(self.feeds)


def get_feeds_from_opml(opml_file):
    result = listparser.parse(opml_file)
    feeds = [feed.url for feed in result.feeds]
    return feeds


def get_posts_from_feed_list(feed_list):
    posts = []
    for feed in feed_list:
        # print('*******FEED******')
        # print(feed)
        d = feedparser.parse(feed)
        for entry in d.entries:
            try:
                if hasattr(entry, 'published_parsed'):
                    pub_date = entry.published_parsed
                elif hasattr(entry, 'updated_parsed'):
                    pub_date = entry.updated_parsed
                else:
                    pub_date = None
                posts.append({'url': entry.link, 'title': entry.title, 'pub_date': pub_date})
            except:
                print(feed)
    return posts


def get_post_text(url):

    try:
        response = requests.get(url)
        doc = Document(response.text)
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text_maker.ignore_images = True
        text = text_maker.handle(doc.summary())
        return text
    except:
        print('REQUESTS ERROR: ', url)



def generate_post_data(post):
    url = post['url']
    text = get_post_text(url)

    return {'title': post['title'],
            'url': url,
            'pub_date': post['pub_date'],
            'text': text}


def combine_post_data(posts):
    post_list = []
    for post in posts:
        try:
            post_list.append(generate_post_data(post))
        except:
            print('moving on...')

    return post_list


def add_post_data_to_db(feeds, collection):
    posts = get_posts_from_feed_list(feeds)

    for post in posts:
        if not collection.find_one({'url': post['url']}):
            collection.insert_one(generate_post_data(post))
        # else:
        #     print('EXISTS: ', post['url'])

    return


# feeds = ['http://www.erogol.com/feed/',
#              'http://logicx24.github.io/feed.xml',
#              ]

# print(combine_post_data(get_posts_from_feed_list(feeds)))

