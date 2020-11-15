import requests
from bs4 import BeautifulSoup
import feedparser
import datetime
import pandas as pd
import openpyxl
import pytz

#page = open("prettified.txt", "a", encoding = "utf-8")
def parseRSSfeeds():
    CBC_feeds = [{"Top Stories":"https://www.cbc.ca/cmlink/rss-topstories"},
                 {"World News":"https://rss.cbc.ca/lineup/world.xml"},
                 {"Technology":"https://rss.cbc.ca/lineup/technology.xml"},
                 {"Politics":"https://rss.cbc.ca/lineup/politics.xml"},
                 {"Arts":"https://rss.cbc.ca/lineup/arts.xml"},
    ]

    Guardian_feeds = [{"World News":"https://www.theguardian.com/world/rss"},
                      {"Global Development":"https://www.theguardian.com/global-development/rss"},
                      {"Business":"https://www.theguardian.com/uk/business/rss"},
                      {"Technology":"https://www.theguardian.com/uk/technology/rss"},
                      {"Environment":"https://www.theguardian.com/uk/environment/rss"},
    ]

    CTV_feeds = [{"Top Stories":"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"},
                 {"World News":"https://www.ctvnews.ca/rss/ctvnews-ca-world-public-rss-1.822289"},
                 {"Politics":"https://www.ctvnews.ca/rss/ctvnews-ca-politics-public-rss-1.822302"},
                 {"Canada News":"https://www.ctvnews.ca/rss/ctvnews-ca-canada-public-rss-1.822284"},
    ]

    news_list = []

    for single_cbc_feed in CBC_feeds:                      #parses all the CBC feeds
        for category, url in single_cbc_feed.items():
            CBC_parsed = feedparser.parse(url)
            articles = CBC_parsed['entries']
            for article in articles:
                news_item = {}
                if "\u200b" in article.title:
                    news_item["headline"] = (article.title).replace("\u200b", "")     #replaces zero-width spaces
                else:
                    news_item["headline"] = article.title
                news_item["link"] = article.link
                news_item["date"] = datetime.datetime(*article.published_parsed[:-3])
                if (BeautifulSoup(article.summary, features='lxml')).find('img')['src']:
                    news_item["image_url"] = (BeautifulSoup(article.summary, features='lxml')).find('img')['src']  #finds the image url in article.summary
                else:
                    news_item["image_url"] = ""
                news_item["publisher"] = "CBC News"     #CBC because all the feeds in this loop are CBC
                if BeautifulSoup(article.summary, features='lxml').find('p').getText():
                    news_item["description"] = BeautifulSoup(article.summary, features='lxml').find('p').getText()
                else:
                    news_item['description'] = ""
                news_item["category"] = category
                news_list.append(news_item)


    for single_guardian_feed in Guardian_feeds:                      #parses all the CBC feeds
        for category, url in single_guardian_feed.items():
            Guardian_parsed = feedparser.parse(url)
            articles = Guardian_parsed['entries']
            for article in articles:
                news_item = {}
                if "\u200b" in article.title:
                    news_item["headline"] = (article.title).replace("\u200b", "")     #replaces zero-width spaces
                else:
                    news_item["headline"] = article.title
                news_item["link"] = article.link
                news_item["date"] = datetime.datetime(*article.published_parsed[:-3])
                if article.media_content[1]["url"]:
                    news_item["image_url"] = article.media_content[1]["url"]                   #finds the image url in article.summary.
                else:                                                                          #There are two media content tags so the [1] targets the second which is higher quality
                    news_item["image_url"] = ""
                news_item["publisher"] = "Guardian"                  #Guardian because all the feeds in this loop are Guardian
                if BeautifulSoup(article.summary, features='lxml').find('p').getText():
                    news_item["description"] = BeautifulSoup(article.summary, features='lxml').find('p').getText()
                else:
                    news_item['description'] = ""
                news_item["category"] = category
                news_list.append(news_item)

    for single_ctv_feed in CTV_feeds:
        for category, url in single_ctv_feed.items():
            CTV_parsed = feedparser.parse(url)
            articles = CTV_parsed['entries']
            for article in articles:
                news_item = {}
                if "\u200b" in article.title:
                    news_item["headline"] = (article.title).replace("\u200b", "")   #replaces zero-width spaces
                else:
                    news_item["headline"] = article.title
                news_item["link"] = article.link
                news_item["date"] = datetime.datetime(*article.published_parsed[:-3])
                if article.links[1]["href"]:
                    news_item["image_url"] = article.links[1]["href"]  #finds the image href in article.links
                else:
                    news_item["image_url"] = ""
                news_item["publisher"] = "CTV News"     #CTV because all the feeds in this loop are CTV
                if BeautifulSoup(article.summary, features='lxml').find('p').getText():
                    news_item["description"] = BeautifulSoup(article.summary, features='lxml').find('p').getText()
                else:
                    news_item['description'] = ""
                news_item["category"] = category
                news_list.append(news_item)


    return news_list

if __name__ == "__main__":
    parseRSSfeeds()

#news_list = sorted(news_list, key = lambda date: date["Date of Publish"])    #sorts by date
#database = pd.DataFrame(news_list, columns = ["Title", "Link", "Date of Publish", "Writer/Author", "Publisher", "Description"])
#database.to_excel("CBC-RSS-FEED.xlsx", index = False, encoding= "utf-8")
#page.write(CBC_soup.prettify())



