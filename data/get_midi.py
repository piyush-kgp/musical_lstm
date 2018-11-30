from bs4 import BeautifulSoup as bs
import urllib
import re
import os

url = 'https://www.cse.iitk.ac.in/users/tvp/music/'
soup = bs(urllib.request.urlopen(urllib.request.Request(url)))
links = soup.find_all('a')
midi_links = [url+link['href'] for link in links if link['href'].endswith('.mid')]

for midi_link in midi_links:
    try:
        file_path = 'midi_files/indian_classical/' + ' '.join(midi_link.split('/')[-2:])
        urllib.request.urlretrieve(midi_link, file_path)
    except:
        print('Could not Download %s' %midi_link)
