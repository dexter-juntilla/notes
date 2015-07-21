import random
import requests
from bs4 import BeautifulSoup
from os.path import basename

def page_crawler( max_pages ):
	page = 1
	while page <= max_pages:
		
		if page == 1:
			url = r"http://www.it-ebooks.info/search/?q=python&type=title"
		else:
			url = r"http://www.it-ebooks.info/search/?q=python&type=title&page=" + str( page )
		
		source_code = requests.get( url ) #get source code as requests.models.Response object
		plain_text = source_code.text #get the text of that object
		soup = BeautifulSoup( plain_text, "lxml" ) #convert the text to BeautifulSoup object

		for link in soup.findAll('a'): #('a', {'class':'item-name'})
			href = r"http://www.it-ebooks.info" + link.get( 'href' )
			print( href )

		page += 1

page_crawler(1)