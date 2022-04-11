from BeautifulSoup import BeautifulSoup

html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>'''

soup = BeautifulSoup(html)

for a in soup.find_all('a', href=True):
    print "Found the URL:", a['href']