from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))
# <html><head></head><body>Sacré bleu!</body></html>

"""
html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>'''

soup = BeautifulSoup(html)

for a in soup.find_all('a', href=True):
    print "Found the URL:", a['href']
"""