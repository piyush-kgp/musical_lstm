from bs4 import BeautifulSoup as bs
import urllib
import re

url = 'https://www.cse.iitk.ac.in/users/tvp/music/'
soup = bs(urllib.request.urlopen(urllib.request.Request(url)))
links = soup.find_all('a')
midi_links = [url+link['href'] for link in links if link['href'].endswith('.mid')]

for midi_link in midi_links:
    try:
        urllib.request.urlretrieve(midi_link,' '.join(midi_link.split('/')[-2:]))
    except:
        print('Could not Download %s' %midi_link)
