# parsing

import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find('table', class_='item_list')
	print (table.prettify())
	
def main():
	print(get_html('http://weblancer.net/projects/'))
	
if __name__ == '__main__':
	main()
	
