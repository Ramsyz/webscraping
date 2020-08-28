import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').read()

soup = bs.BeautifulSoup(source,'lxml')
