import requests;
r=requests.get("http://www.runoob.com/django/django-nginx-uwsgi.html");
r.encoding=r.apparent_encoding;
demo=r.text;
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser');
print(demo)
# soup.prettify()


