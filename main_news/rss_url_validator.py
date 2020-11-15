from bs4 import BeautifulSoup
import requests
import lxml


def validate_url(link):
	link_http = requests.get(link)
	bs4_link = BeautifulSoup(link_http.text, "lxml")
	if bs4_link.find('rss'):
		return True
	else:
		return False

