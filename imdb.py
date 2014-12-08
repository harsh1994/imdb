import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

print "Enter the Movie/TV Series"

movie = raw_input()

payload = {'ref_':'nv_sr_fn','q':movie,'s':'all'}
r = requests.get('http://www.imdb.com/find', params = payload)
URL = r.url
soup = BeautifulSoup(urlopen(URL))



soup1 =  soup.find_all(href=re.compile('fn_al_tt_1'))

for link in soup1:
    x = link.get('href')
    break

a = 'http://www.imdb.com/'+x


r1 = requests.get(a)
URL1 = r1.url
soup2 = BeautifulSoup(urlopen(URL1))

rate = soup2.find('span',itemprop='ratingValue')

print str(rate.contents[0])

