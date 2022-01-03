#!/usr/bin/env python
# coding: utf-8

# In[1]:
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:
html = urlopen("http://")


# In[3]:
bs = BeautifulSoup(html.read(), 'html.parser')


# In[4]:
print(bs.h1)


# In[5]:
html = urlopen("http://www.pythonscraping.com/pages/page1.html")  # html 매번 다시해줘야 제대로 작동하는듯


# In[6]:
bs = BeautifulSoup(html, 'html.parser')  # html.parser: 구문분석기


# In[7]:
print(bs.html.h1)


# In[8]:
from urllib.request import HTTPError  # 페이지를 찾을 수 없어~: URL 해석시 에러 생기는 경우 발생하는 에러


# In[9]:
try:
    html = urlopen("http://")
except HTTPError as e:
    print(e)


# In[10]:
from urllib.error import URLError  # 웹페이지 다운됐거나 URL에 오타 있을 때 URLError 발생


# In[11]:
try:
    html = urlopen("https://")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It Worked!")


# In[12]:
print(bs.nonExistentTag)


# In[13]:
print(bs.nonExistentTag.someTag)  # 존재하지 않는 태그 불러서 함수 호출시 발생하는 에러 AttributeError


# In[14]:
try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)


# In[15]:
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://")
if title == None:
    print("Title could not be found")
else:
    print(title)
