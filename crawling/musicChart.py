# melon(https://www.melon.com/)
# music platfrom address

import requests
from bs4 import BeautifulSoup

# request = requests.get('https://www.melon.com/chart/index.htm')
# print(request) # <Response [406]> : Unable to read header information. Page Connection Failed
# https://kkyunstory.tistory.com/95

# When Web site data cannot be imported because of header information
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
request = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0900', headers = header)
# print(request)
html = request.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
title = soup.findAll('div', {'class': 'rank01'})
# print(title)
artist = soup.findAll('span', {'class': 'checkEllipsis'})

"""
for i in range(len(title)):
    titles = title[i].text.strip()
    artists = artist[i].text.strip()
    # print(titles)
    # print(artists)
    print('{0:3d}위 {1} - {2}'.format(i+1, artists, titles))
"""


file = open('melonAbroadTop100.txt', 'w', -1, 'UTF-8')

for i in range(len(title)):
    titles = title[i].text.strip()
    artists = artist[i].text.strip()
    data = '{0:3d}위 {1} - {2}'.format(i+1, artists, titles)
    file.write(data + '\n')
print("Completed writing file!!")
file.close()



file = open('melonAbroadTop100.txt', 'r', -1, 'UTF-8')
lines = file.readlines()
print("Melon Music Overseas TOP 100")
for line in lines:
    print(line, end='')
file.close()
